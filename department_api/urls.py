from django.urls import path

from .views import DepartmentListView, DepartmentDetailView, EmployeeListView, EmployeeDetailView


urlpatterns = [
    path('departments/', DepartmentListView.as_view()),
    path('departments/<str:slug>/', DepartmentDetailView.as_view()),
    path('employees/', EmployeeListView.as_view()),
    path('employees/<int:pk>', EmployeeDetailView.as_view())
]
