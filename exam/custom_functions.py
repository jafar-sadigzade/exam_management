import csv
from io import StringIO, TextIOWrapper

from django.utils import timezone

from .models import Student, ColumnMapping


def replace_letters(text):
    replacements = {
        "e": "Ə",
        "s": "Ş",
        "g": "Ğ",
        "u": "Ü",
        "i": "İ",
        "o": "Ö",
        "c": "Ç"
    }

    for key, value in replacements.items():
        text = text.replace(key, value)

    return text


def generate_unique_student_id(length=7):
    import random
    import string
    while True:
        random_string = ''.join(random.choices(string.digits, k=length))
        if not Student.objects.filter(student_id=random_string).exists():
            return random_string


def get_column_mapping(exam):
    try:
        mapping = exam.exam.column_mapping
        return {
            "first_name": mapping.first_name,
            "last_name": mapping.last_name,
            "father_name": mapping.father_name,
            "gender": mapping.gender,
            "student_id": mapping.student_id,
            "answers": mapping.answers
        }
    except ColumnMapping.DoesNotExist:
        raise ValueError("Column mapping does not exist for this exam.")


def process_student_data(file, exam):
    try:
        # Clear existing student data for the given exam
        Student.objects.filter(exam=exam).delete()
        column_mapping = get_column_mapping(exam)
    except ValueError as e:
        print(f"Error: {e}")
        return

    if isinstance(file, TextIOWrapper):
        file_content = file.read()
    else:
        file_content = file.read().decode('utf-8')

    reader = csv.reader(StringIO(file_content))

    correct_answers_dict = {subject['subject_name']: subject['correct_answers'] for subject in
                            exam.correct_answers['subjects']}

    for row in reader:
        student_id = row[column_mapping['student_id']]

        # Ensure unique student ID
        while Student.objects.filter(student_id=student_id, exam=exam).exists():
            student_id = generate_unique_student_id()

        try:
            # Create answers_dict in the required format
            subjects_list = []
            start_point = 0
            for subject in exam.exam.scoring_rules['scoring_rules']:
                subject_name = subject['subject_name']
                question_count = subject['question_count']
                student_answers = row[column_mapping["answers"]][start_point:start_point + question_count]
                start_point += question_count
                correct_answers = correct_answers_dict.get(subject_name, "")
                subjects_list.append({
                    "subject_name": subject_name,
                    "student_answers": student_answers,
                    "correct_answers": correct_answers
                })

            student_info = {
                "first_name": replace_letters(row[column_mapping['first_name']].strip()),
                "last_name": replace_letters(row[column_mapping['last_name']].strip()),
                "father_name": replace_letters(row[column_mapping['father_name']].strip()),
                "gender": row[column_mapping['gender']],
                "student_id": student_id,
                "subjects": subjects_list  # Store answers as a list of dictionaries
            }

            student = Student.objects.create(
                first_name=student_info['first_name'],
                last_name=student_info['last_name'],
                father_name=student_info['father_name'],
                gender=student_info['gender'],
                student_id=student_info['student_id'],
                exam=exam,
                answers=student_info['subjects']  # Use new format
            )

            student.results = calculate_student_result(student, exam)

            if student.results:
                student.total_score = student.results['total_score']
            student.processed_at = timezone.now()
            student.save()

        except Exception as e:
            print(f"Error processing row {row}: {e}")


def calculate_student_result(student, exam):
    try:
        subject_scores = {}
        total_score = 0.0

        # Ensure that student.answers is a list of dictionaries
        if isinstance(student.answers, list):
            subjects_list = student.answers
        else:
            raise ValueError(f"Expected a list for student.answers but got {type(student.answers)}")

        # Iterate through subjects in the exam structure
        for subject in exam.exam.scoring_rules['scoring_rules']:
            subject_name = subject['subject_name']
            correct_answers = next(
                (sub['correct_answers'] for sub in exam.correct_answers['subjects'] if
                 sub['subject_name'] == subject_name),
                None
            )

            if correct_answers is None:
                raise ValueError(f"No correct answers found for subject {subject_name}")

            # Find the subject data in the student's answers
            subject_data = next((sub for sub in subjects_list if sub['subject_name'] == subject_name), None)

            if subject_data is None:
                raise ValueError(f"No data found for subject {subject_name}")

            student_answers = subject_data['student_answers']

            # Ensure correct and student answers are the same length
            correct_answers = correct_answers
            student_answers = student_answers

            # Calculate the correct and incorrect answers count
            correct_count = 0
            incorrect_count = 0

            for sa, ca in zip(student_answers, correct_answers):
                if sa == ' ':
                    pass
                elif sa == ca or ca == '*':
                    correct_count += 1
                elif sa != ca:
                    incorrect_count += 1

            # Calculate the total score for the subject
            total_score_for_subject = (correct_count * subject['points_per_correct']) + (
                    incorrect_count * subject['points_per_incorrect'])

            # Ensure the score is not negative
            total_score_for_subject = max(total_score_for_subject, 0)

            subject_scores[subject_name] = {
                "right_answers": correct_count,
                "wrong_answers": incorrect_count,
                "total": total_score_for_subject
            }

            total_score += total_score_for_subject

        return {
            "subject_scores": subject_scores,
            "total_score": total_score
        }
    except Exception as e:
        print(f"Error calculating result for student {student.student_id}: {e}")
        return None
