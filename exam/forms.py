from django import forms

from .models import Exam


class UploadFileForm(forms.Form):
    file = forms.FileField()


class ExamForm(forms.ModelForm):
    class Meta:
        model = Exam
        fields = ['exam', 'txt', 'correct_answers']
