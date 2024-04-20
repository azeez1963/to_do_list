from django import forms
from .models import Task


class FormModel(forms.ModelForm):
      class Meta:
            model = Task
            fields =['tittle']