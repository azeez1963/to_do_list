from django.shortcuts import render
from .models import Task

# Create your views here.

def home_page_view(request):
      name = 'Azeez'
      context ={
            'name': name
      }

      return render(request, 'main/index.html', context)