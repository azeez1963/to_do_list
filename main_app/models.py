from django.db import models

# Create your models here.

class Task(models.Model):
      tittle = models.CharField(max_length=250)
      date_posted = models.DateField(auto_now_add=True)

      def __str__(self):
            return self.tittle