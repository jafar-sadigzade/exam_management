from django.contrib import admin

from .custom_functions import process_student_data
from .models import Exam, ExamModel, ColumnMapping, Student


class ColumnMappingInline(admin.TabularInline):
    model = ColumnMapping
    extra = 1


class ExamModelAdmin(admin.ModelAdmin):
    inlines = [ColumnMappingInline]
    list_display = ('exam_name', 'created_at')


class ExamAdmin(admin.ModelAdmin):
    list_display = ('exam', 'created_at')

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        # Process the student data after saving the Exam instance
        process_student_data(obj.txt, obj)


admin.site.register(ExamModel, ExamModelAdmin)
admin.site.register(Exam, ExamAdmin)
admin.site.register(Student)
