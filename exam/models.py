from django.db import models


class ExamModel(models.Model):
    exam_name = models.CharField(max_length=255, verbose_name="İmtahan adı")
    scoring_rules = models.JSONField(verbose_name="Qaydalar")
    created_at = models.DateTimeField(auto_now_add=True, blank=True, verbose_name="Yaradılma tarixi")

    def __str__(self):
        return self.exam_name

    class Meta:
        verbose_name = 'İmtahan modeli'
        verbose_name_plural = 'İmtahan modelləri'


class ColumnMapping(models.Model):
    exam = models.OneToOneField(ExamModel, on_delete=models.CASCADE, related_name='column_mapping')
    first_name = models.PositiveIntegerField()
    last_name = models.PositiveIntegerField()
    father_name = models.PositiveIntegerField()
    class_no = models.PositiveIntegerField()
    student_id = models.PositiveIntegerField()
    answers = models.PositiveIntegerField()

    def __str__(self):
        return self.exam.exam_name


class Exam(models.Model):
    exam = models.ForeignKey(ExamModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, verbose_name="İmtahan adı")
    txt = models.FileField(upload_to='exams/txt/', verbose_name="Optik oxuyucudan çıxan fayl")
    correct_answers = models.JSONField(verbose_name="Düzgün cavablar")
    created_at = models.DateTimeField(auto_now_add=True, blank=True, verbose_name="Yaradılma tarixi")

    def __str__(self):
        return f"Model: {self.exam.exam_name} - {self.name}"

    class Meta:
        verbose_name = 'İmtahan'
        verbose_name_plural = 'İmtahanlar'


class Student(models.Model):
    first_name = models.CharField(max_length=255, verbose_name="Şagirdin adı")
    last_name = models.CharField(max_length=255, verbose_name="Şagirdin soyadı")
    father_name = models.CharField(max_length=255, verbose_name="Şagirdin ata adı")
    class_no = models.CharField(max_length=2, default=0, verbose_name="Oxuduğu sinif")
    total_score = models.FloatField(default=0, verbose_name="Ümumi bal")
    student_id = models.CharField(max_length=255, unique=True, verbose_name="İş nömrəsi")
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    answers = models.JSONField(verbose_name="Cavab")
    results = models.JSONField(null=True, blank=True, verbose_name="Nəticə")
    processed_at = models.DateTimeField(null=True, blank=True, verbose_name="Yüklənmə tarixi")

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.student_id}"

    class Meta:
        verbose_name = 'Şagird'
        verbose_name_plural = 'Şagirdlər'
