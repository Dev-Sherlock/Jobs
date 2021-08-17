from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Job(models.Model):
    title=models.CharField(max_length=50,blank=True)
    author = models.OneToOneField(User,on_delete=models.CASCADE)
    # author=models.CharField(max_length=100,blank=True)
    date=models.DateField(auto_now_add=True)
    description=models.TextField(blank=True)

    def __str__(self):
        return self.title
