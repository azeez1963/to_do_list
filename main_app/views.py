from django.shortcuts import render, redirect
from .models import Task
from .forms import FormModel

# Create your views here.

def home_page_view(request):
      all_task = Task.objects.all()
      return render(request, 'main/index.html', {"task": all_task})

def create_task(request):
     all_task = Task.objects.all()
     if request.method == 'POST':
           form = FormModel(request.POST)
           if form.is_valid():
                 form.save()
           return redirect('home')
     else:
       form = FormModel()
       context={
            'all_task':all_task,
            'form':form
       }
       return render(request, 'main/createtask.html', context)