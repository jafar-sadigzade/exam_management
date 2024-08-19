from django.urls import path

from . import views

urlpatterns = [
    path('', views.exam_request),
    path('exam/<int:exam_id>/results/table', views.exam_results_table, name='exam_results_table'),
    path('exam/<int:exam_id>/results/report', views.exam_results_report, name='exam_results_report'),
]
