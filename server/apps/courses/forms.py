from django import forms
from .models import LessonFile

class LessonFileForm(forms.ModelForm):
    class Meta:
        model = LessonFile
        fields = ['lesson', 'file_type', 'file']
