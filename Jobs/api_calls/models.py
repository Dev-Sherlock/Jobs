from django.db import models

# Create your models here.

class Job(models.Model):
    title=models.CharField(max_length=50,blank=True)
    date=models.DateField(auto_now_add=True)
    description=models.TextField(blank=True)
