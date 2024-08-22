from django.shortcuts import render, get_object_or_404

from .models import Exam, Student


def index(request):
    exams = Exam.objects.all()
    return render(request, 'exam/index.html', {'exams': exams})


def get_student_report(exam, student_id, gender, template_name):
    pdf = f'/static/pdf/{student_id}.pdf'

    try:
        # Get the list of students ordered by total_score
        students_ordered = Student.objects.filter(exam=exam, gender=gender).order_by('-total_score')
        student = students_ordered.get(student_id=student_id)
        student_index = list(students_ordered).index(student) + 1

        # Check the score of the 30th student
        if student_index <= 30:
            message = "Qəbul oldunuz!"
            tags = "alert-success"
        else:
            thirtieth_student = students_ordered[29]  # 30th student (index 29 because it's 0-based index)
            if student.total_score == thirtieth_student.total_score:
                message = "Qəbul oldunuz!"
                tags = "alert-success"
            else:
                message = "Qəbul olmadınız!"
                tags = "alert-danger"

        return {
            'student': student,
            'rank': student_index,
            'pdf': pdf,
            'message': message,
            "tags": tags
        }
    except Student.DoesNotExist:
        return {'error': 'İş nömrəsi tapılmadı!'}
    except Exam.DoesNotExist:
        return {'error': 'İmtahan tapılmadı!'}


def report_view(request, gender, template_name):
    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        exam = get_object_or_404(Exam, id=2)
        context = get_student_report(exam, student_id, gender, template_name)
        return render(request, template_name, context)
    return render(request, 'exam/input_id.html')


def boy_report(request):
    return report_view(request, 'K', 'exam/exam_results_report_student.html')


def girl_report(request):
    return report_view(request, 'Q', 'exam/exam_results_report_student.html')


def exam_results_table(request, exam_id, gender, template_name):
    exam = get_object_or_404(Exam, id=exam_id)
    students = Student.objects.filter(exam=exam, gender=gender).order_by('-total_score')
    return render(request, template_name, {'exam': exam, 'students': students})


def exam_results_table_girl(request, exam_id):
    return exam_results_table(request, exam_id, 'Q', 'exam/exam_results_table.html')


def exam_results_table_boy(request, exam_id):
    return exam_results_table(request, exam_id, 'K', 'exam/exam_results_table.html')


def exam_results_report(request, exam_id, gender, template_name):
    exam = get_object_or_404(Exam, id=exam_id)
    students = Student.objects.filter(exam=exam, gender=gender).order_by('-total_score')
    return render(request, template_name, {'exam': exam, 'students': students})


def exam_results_report_girl(request, exam_id):
    return exam_results_report(request, exam_id, 'Q', 'exam/exam_results_report.html')


def exam_results_report_boy(request, exam_id):
    return exam_results_report(request, exam_id, 'K', 'exam/exam_results_report.html')
