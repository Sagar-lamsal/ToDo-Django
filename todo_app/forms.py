from .models import task
from django import forms

class taskinput(forms.ModelForm):
    class Meta:
        model = task
        fields=['tasks']
        labels={
            'tasks' : '',
        }