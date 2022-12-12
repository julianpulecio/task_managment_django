from django.db import models


class Employee(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=254)
