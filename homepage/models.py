from django.db import models

# Create your models here.
class Mentor (models.Model):
    menid=models.CharField(max_length=3, primary_key=True)
    menname=models.TextField(max_length=225)
    menroomno=models.CharField(max_length=3, default='sk2')

class Course(models.Model):
    code = models.CharField(max_length=6, primary_key = True)
    description = models.TextField()