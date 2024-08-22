from django.shortcuts import render, get_object_or_404

from .models import Exam, Student


def index(request):
    exams = Exam.objects.all()
    return render(request, 'exam/index.html', {'exams': exams})


def get_student_report(exam, student_id, gender, template_name):
    img = f'/static/pdf/{student_id}.pdf'

    try:
        students_ordered = Student.objects.filter(exam=exam, gender=gender).order_by('-total_score')
        student = students_ordered.get(student_id=student_id)
        student_index = list(students_ordered).index(student) + 1
        return {
            'student': student,
            'rank': student_index,
            'img': img
        }
    except Student.DoesNotExist:
        return {'error': 'İş nömrəsi tapılmadı! '}
    except Exam.DoesNotExist:
        return {'error': 'İmtahan tapılmadı! '}


def report_view(request, gender, template_name):
    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        exam = get_object_or_404(Exam, id=1)
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
