from rest_framework import serializers

from department.models import Department, Employee


class DepartmentSerializer(serializers.ModelSerializer):
    employees = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Department
        fields = ('title', 'description', 'slug', 'employees')
        lookup_field = 'slug'


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('first_name', 'last_name', 'date_of_birth', 'salary', 'department')
