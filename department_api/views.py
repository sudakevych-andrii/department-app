from rest_framework import generics

from department.models import Department, Employee
from .serializers import DepartmentSerializer, EmployeeSerializer


class DepartmentListView(generics.ListCreateAPIView):
    queryset = Department.objects.all().order_by('title')
    serializer_class = DepartmentSerializer


class DepartmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    lookup_field = 'slug'


class EmployeeListView(generics.ListCreateAPIView):
    queryset = Employee.objects.all().order_by('first_name', 'last_name')
    serializer_class = EmployeeSerializer


class EmployeeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
