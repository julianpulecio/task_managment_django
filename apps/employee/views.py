from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from drf_yasg.utils import swagger_auto_schema
from apps.employee.serializer import EmployeeSerializer, PatchEmployeeSerializer
from apps.employee.models import Employee


class EmployeeView(ViewSet):
    def list(self, request):
        queryset = Employee.objects.all()
        employees_serialized = EmployeeSerializer(queryset, many=True)
        return Response(employees_serialized.data)

    @swagger_auto_schema(request_body=EmployeeSerializer)
    def create(self, request):
        serialized_data = EmployeeSerializer(data=request.data)
        serialized_data.is_valid(raise_exception=True)
        employee = serialized_data.create(serialized_data.validated_data)
        employee_serialized = EmployeeSerializer(employee)
        return Response(employee_serialized.data)

    def retrieve(self, request, pk=None):
        queryset = Employee.objects.all()
        employee = get_object_or_404(queryset, pk=pk)
        employee_serialized = EmployeeSerializer(employee)
        return Response(employee_serialized.data)

    @swagger_auto_schema(request_body=EmployeeSerializer)
    def update(self, request, pk=None):
        queryset = Employee.objects.all()
        employee = get_object_or_404(queryset, pk=pk)
        employee_serialized = EmployeeSerializer(employee, data=request.data, partial=False)
        employee_serialized.is_valid(raise_exception=True)
        employee_serialized.save()
        return Response(employee_serialized.data)

    @swagger_auto_schema(request_body=PatchEmployeeSerializer)
    def partial_update(self, request, pk=None):
        queryset = Employee.objects.all()
        employee = get_object_or_404(queryset, pk=pk)
        employee_serialized = EmployeeSerializer(employee, data=request.data, partial=True)
        employee_serialized.is_valid(raise_exception=True)
        employee_serialized.save()
        return Response(employee_serialized.data)

    def destroy(self, request, pk=None):
        queryset = Employee.objects.all()
        employee = get_object_or_404(queryset, pk=pk)
        employee.delete()
        return Response('Department was destroyed successfully')