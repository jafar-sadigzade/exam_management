from django.db import models


class ExamModel(models.Model):
    exam_name = models.CharField(max_length=255)
    scoring_rules = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.exam_name


class ColumnMapping(models.Model):
    exam = models.OneToOneField(ExamModel, on_delete=models.CASCADE, related_name='column_mapping')
    first_name = models.PositiveIntegerField()
    last_name = models.PositiveIntegerField()
    father_name = models.PositiveIntegerField(null=True, blank=True)
    class_no = models.PositiveIntegerField(null=True, blank=True)
    other_info = models.JSONField(null=True, blank=True)
    student_id = models.PositiveIntegerField()
    answers = models.PositiveIntegerField()

    def __str__(self):
        return self.exam.exam_name


class Exam(models.Model):
    exam = models.ForeignKey(ExamModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=True, blank=True)
    txt = models.FileField(upload_to='exams/txt/')
    correct_answers = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.exam.exam_name


class Student(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    father_name = models.CharField(max_length=255)
    class_no = models.CharField(max_length=2)
    total_score = models.FloatField(default=0)
    student_id = models.CharField(max_length=255, unique=True)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    answers = models.JSONField()  # Stores the answers given by the student as a JSON field
    results = models.JSONField(null=True, blank=True)  # Stores the calculated results as JSON
    processed_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.student_id}"
