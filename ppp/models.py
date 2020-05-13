from __future__ import unicode_literals
from django.db import models

class Student(models.Model):
 first_name=models.CharField(max_length=30)
 last_name=models.CharField(max_length=30)
 image=models.ImageField(upload_to='media')
 