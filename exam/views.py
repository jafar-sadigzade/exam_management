from django.shortcuts import render, redirect

from .models import Exam, Student


def exam_request(request):
    exams = Exam.objects.all()
    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        img = '/static/images/' + student_id + '.png'

        try:
            exam = Exam.objects.get(id=2)
            students_ordered = Student.objects.filter(exam=exam).order_by('-total_score')
            student = students_ordered.get(student_id=student_id)
            student_index = list(students_ordered).index(student) + 1
            context = {'student': student, 'rank': student_index, 'img': img}
            return render(request, 'exam/exam_results_report_student.html', context)
        except (Student.DoesNotExist, Exam.DoesNotExist):
            context = {'error': 'İş nömrəsi tapılmadı! '}
            return render(request, 'exam/exam_results_report_student.html', context)
    return render(request, 'exam/exam_list.html', {'exams': exams})


def exam_results_table(request, exam_id):
    try:
        exam = Exam.objects.get(id=exam_id)
        students = Student.objects.filter(exam=exam)
    except Exam.DoesNotExist:
        return redirect('exam_request')  # Redirect if exam is not found
    return render(request, 'exam/exam_results_table.html', {'exam': exam, 'students': students})


def exam_results_report(request, exam_id):
    try:
        exam = Exam.objects.get(id=exam_id)
        students = Student.objects.filter(exam=exam)
    except Exam.DoesNotExist:
        return redirect('exam_request')  # Redirect if exam is not found
    return render(request, 'exam/exam_results_report.html', {'exam': exam, 'students': students})
