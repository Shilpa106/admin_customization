# from turtle import title
from django.db import models

# Create your models here.
class Author(models.Model):
    name=models.CharField(max_length=50, null=True,blank=True)
    title=models.CharField(max_length=50, null=True,blank=True)
    view_birth_date=models.DateField(null=True, blank=True)
    