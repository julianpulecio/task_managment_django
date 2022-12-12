from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from apps.project.models import Project
from apps.project.serializer import ProjectSerializer


class ProjectView(ViewSet):
    def list(self, request):
        queryset = Project.objects.all()
        tasks_serialized = ProjectSerializer(queryset, many=True)
        return Response(tasks_serialized.data)

    @swagger_auto_schema(request_body=ProjectSerializer)
    def create(self, request):
        serialized_data = ProjectSerializer(data=request.data)
        serialized_data.is_valid(raise_exception=True)
        project = serialized_data.create(validated_data=serialized_data.validated_data)
        project.save()
        project_serialized = ProjectSerializer(project)
        return Response(project_serialized.data)

    def retrieve(self, request, pk=None):
        queryset = Project.objects.all()
        task = get_object_or_404(queryset, pk=pk)
        task_serialized = ProjectSerializer(task)
        return Response(task_serialized.data)

    @swagger_auto_schema(request_body=ProjectSerializer)
    def update(self, request, pk=None):
        queryset = Project.objects.all()
        task = get_object_or_404(queryset, pk=pk)
        project_serialized = ProjectSerializer(task, data=request.data, partial=False)
        project_serialized.is_valid(raise_exception=True)
        project_serialized.save()
        return Response(project_serialized.data)

    @swagger_auto_schema(request_body=ProjectSerializer)
    def partial_update(self, request, pk=None):
        queryset = Project.objects.all()
        project = get_object_or_404(queryset, pk=pk)
        project_serialized = ProjectSerializer(project, data=request.data, partial=True)
        project_serialized.is_valid(raise_exception=True)
        project_serialized.update(project, validated_data=project_serialized.validated_data)
        return Response(project_serialized.data)

    def destroy(self, request, pk=None):
        queryset = Project.objects.all()
        project = get_object_or_404(queryset, pk=pk)
        project.delete()
        return Response('Project was destroyed successfully')
