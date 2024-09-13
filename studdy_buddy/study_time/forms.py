from django import forms
from .models import StudyTime, StudyMaterial

class StudyTimeForm(forms.ModelForm):
    class Meta:
        model = StudyTime
        fields = ['subject', 'time']

class StudyMaterialForm(forms.ModelForm):
    class Meta:
        model = StudyMaterial
        fields = ['name', 'file']
