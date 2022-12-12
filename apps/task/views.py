from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from apps.task.models import Task
from apps.task.serializer import TaskSerializer


class TaskView(ViewSet):
    def list(self, request):
        queryset = Task.objects.all()
        tasks_serialized = TaskSerializer(queryset, many=True)
        return Response(tasks_serialized.data)

    @swagger_auto_schema(request_body=TaskSerializer)
    def create(self, request):
        serialized_data = TaskSerializer(data=request.data)
        serialized_data.is_valid(raise_exception=True)
        task = serialized_data.create(validated_data=serialized_data.validated_data)
        task.save()
        task_serialized = TaskSerializer(task)
        return Response(task_serialized.data)

    def retrieve(self, request, pk=None):
        queryset = Task.objects.all()
        task = get_object_or_404(queryset, pk=pk)
        task_serialized = TaskSerializer(task)
        return Response(task_serialized.data)

    @swagger_auto_schema(request_body=TaskSerializer)
    def update(self, request, pk=None):
        queryset = Task.objects.all()
        task = get_object_or_404(queryset, pk=pk)
        task_serialized = TaskSerializer(task, data=request.data, partial=False)
        task_serialized.is_valid(raise_exception=True)
        task_serialized.save()
        return Response(task_serialized.data)

    @swagger_auto_schema(request_body=TaskSerializer)
    def partial_update(self, request, pk=None):
        queryset = Task.objects.all()
        task = get_object_or_404(queryset, pk=pk)
        task_serialized = TaskSerializer(task, data=request.data, partial=True)
        task_serialized.is_valid(raise_exception=True)
        task_serialized.update(task,validated_data=task_serialized.validated_data)
        return Response(task_serialized.data)

    def destroy(self, request, pk=None):
        queryset = Task.objects.all()
        task = get_object_or_404(queryset, pk=pk)
        task.delete()
        return Response('Department was destroyed successfully')