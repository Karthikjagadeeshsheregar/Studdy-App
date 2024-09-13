from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class StudyTime(models.Model):
    subject = models.CharField(max_length=100)
    time = models.TimeField()

    def __str__(self):
        return f"{self.subject} - {self.time}"

class StudyMaterial(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='sankalp')

    def __str__(self):
        return self.name
