from django.contrib import admin

from .custom_functions import process_student_data
from .models import Exam, ExamModel, ColumnMapping, Student


class ColumnMappingInline(admin.TabularInline):
    model = ColumnMapping
    extra = 1


@admin.register(ExamModel)
class ExamModelAdmin(admin.ModelAdmin):
    inlines = [ColumnMappingInline]
    list_display = ('exam_name', 'created_at')


@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ('exam', 'name', 'created_at')
    list_editable = ('name',)

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        # Process the student data after saving the Exam instance
        process_student_data(obj.txt, obj)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'first_name', 'last_name', 'father_name', 'class_no', 'total_score')
    list_filter = ('student_id', 'first_name', 'last_name', 'class_no', 'total_score')
