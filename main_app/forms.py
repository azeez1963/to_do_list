from django.forms import forms
from .models import Task


class FormModel(forms.Form):
      class Meta:
            model = Task
            fields =['tittle']