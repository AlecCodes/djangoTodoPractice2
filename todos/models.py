from django.db import models

# Create your models here.
class Todo(models.model):
    subject = models.CharField(max_length=100)
    detail = models.CharField(max_length=100)