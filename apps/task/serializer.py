from django.forms import model_to_dict
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from datetime import datetime

from apps.employee.models import Employee
from apps.project.models import Project
from apps.task.models import Task


class TaskSerializer(serializers.ModelSerializer):
    employees = serializers.PrimaryKeyRelatedField(queryset=Employee.objects.all(), many=True, required=True,
                                                   allow_empty=False)
    title = serializers.CharField(max_length=255, required=True)
    description = serializers.CharField(required=True)
    start_date = serializers.DateField(required=True, input_formats=['%Y-%m-%d'])
    end_date = serializers.DateField(required=True, input_formats=['%Y-%m-%d'])

    class Meta:
        model = Task
        fields = '__all__'

    def to_representation(self, instance):
        task = super(TaskSerializer, self).to_representation(instance)
        task['start_date'] = datetime.strptime(task['start_date'], '%Y-%m-%d').strftime('%Y-%m-%d %H:%M:%S')
        task['end_date'] = datetime.strptime(task['end_date'], '%Y-%m-%d').strftime('%Y-%m-%d %H:%M:%S')
        task['project'] = model_to_dict(Project.objects.filter(pk=instance.project.pk).first())
        task['employees'] = [model_to_dict(employee) for employee in instance.employees.all()]
        return task

    def validate(self, validated_data):
        if validated_data.get('start_date') > validated_data.get('end_date'):
            raise ValidationError({'end_date': ['The end date must be greater or equal than the start_date']})
        return validated_data
