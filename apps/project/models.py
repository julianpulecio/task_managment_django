from django.core.validators import RegexValidator
from django.db import models


# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=2550)
    description = models.TextField()
    color = models.CharField(max_length=7)
