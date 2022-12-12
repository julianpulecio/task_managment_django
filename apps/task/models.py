from django.db import models
from apps.employee.models import Employee
from apps.project.models import Project


class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    employees = models.ManyToManyField(Employee, related_name="tasks")
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')