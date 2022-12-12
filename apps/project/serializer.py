from django.core.validators import RegexValidator
from rest_framework import serializers
from apps.project.models import Project


class ProjectSerializer(serializers.ModelSerializer):
    color = serializers.CharField(
        max_length=7,
        required=True,
        validators=[RegexValidator('^#(?:[0-9a-fA-F]{3}){1,2}$', message='Color must have hex format')]
    )

    class Meta:
        model = Project
        fields = '__all__'