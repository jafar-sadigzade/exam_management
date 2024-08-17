from django.shortcuts import render

from .models import Exam, Student


def exam_request(request):
    exams = Exam.objects.all()
    context = {'exams': exams}
    return render(request, 'exam/exam_list.html', context)


def exam_results_table(request, exam_id):
    exam = Exam.objects.get(id=exam_id)
    students = Student.objects.filter(exam=exam)
    return render(request, 'exam/exam_results_table.html', {'exam': exam, 'students': students})


def exam_results_report(request, exam_id):
    exam = Exam.objects.get(id=exam_id)
    students = Student.objects.filter(exam=exam)
    return render(request, 'exam/exam_results_report.html', {'exam': exam, 'students': students})
