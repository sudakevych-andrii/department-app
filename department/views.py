from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView, ListView, DetailView

from .models import Department, Employee


class Index(TemplateView):
    pass


class DepartmentListView(ListView):
    model = Department
    context_object_name = 'departments'
    template_name = 'department/departments.html'

    @staticmethod
    def get_average_salary(department):
        if not department.employees.all():
            return 0
        return sum([employee.salary for employee in department.employees.all()]) / len(department.employees.all())

    @staticmethod
    def get_total_salary(department):
        return sum([employee.salary for employee in department.employees.all()])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['departments'] = [
            {
                'department': department,
                'total_salary':  self.get_total_salary(department),
                'average_salary': self.get_average_salary(department)
            }
            for department in context['departments']
        ]
        return context


class DepartmentDetailView(DetailView):
    model = Department
    context_object_name = 'department'
    template_name = 'department/department.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        employees = self.object.employees.all()
        context['employees'] = employees
        return context


class EmployeesListView(ListView):
    model = Employee
    context_object_name = 'employees'
    template_name = 'department/employees.html'


class EmployeesDetailView(DetailView):
    model = Employee
    context_object_name = 'employee'
    template_name = 'department/employee.html'


class CustomLoginView(LoginView):
    template_name = 'department/login.html'
