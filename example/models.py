from django.db import models

# Create your models here.
from mdeditor.fields import MDTextField

class ExampleModel(models.Model):
    name = models.CharField(max_length=10)
    content = MDTextField()

