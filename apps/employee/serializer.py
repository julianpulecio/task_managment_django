from abc import ABC, ABCMeta

from django.forms.models import model_to_dict
from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField
from apps.employee.models import Employee
from apps.task.models import Task
from apps.task.serializer import TaskSerializer


class EmployeeSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(Task, many=True, read_only=True)

    class Meta:
        model = Employee
        fields = '__all__'

    def to_representation(self, instance):
        employee = super(EmployeeSerializer, self).to_representation(instance)
        return employee


class PatchEmployeeSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255, required=False)
    email = serializers.EmailField(required=False)
    last_name = serializers.CharField(max_length=255, required=False)
