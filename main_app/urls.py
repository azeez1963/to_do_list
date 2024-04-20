from django.contrib import admin
from django.urls import path
from .views import home_page_view, create_task


urlpatterns = [
      path('', home_page_view, name='home'),
      path('create-task/', create_task, name ='create_task')
]