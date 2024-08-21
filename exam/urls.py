from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('exam/boy/report', views.boy_report, name='boy_report'),
    path('exam/girl/report', views.girl_report, name='girl_report'),
    path('exam/<int:exam_id>/results/table/girl', views.exam_results_table_girl, name='exam_results_table_girl'),
    path('exam/<int:exam_id>/results/table/boy', views.exam_results_table_boy, name='exam_results_table_boy'),
    path('exam/<int:exam_id>/results/report/girl', views.exam_results_report_girl, name='exam_results_report_girl'),
    path('exam/<int:exam_id>/results/report/boy', views.exam_results_report_boy, name='exam_results_report_boy'),
]
