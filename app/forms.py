from django import forms
from .models import *


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name']


class MarkForm(forms.ModelForm):
    class Meta:
        model = MarkItem
        fields = ['mark', 'day', 'subject', 'student']
