from django.urls import path
from django.contrib.auth.views import LogoutView

from .views import Index, CustomLoginView, DepartmentListView, DepartmentDetailView, EmployeesListView, EmployeesDetailView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('departments/', DepartmentListView.as_view(), name='departments'),
    path('departments/<str:slug>/', DepartmentDetailView.as_view(), name='department'),
    path('employees/', EmployeesListView.as_view(), name='employees'),
    path('employees/<str:slug>/', EmployeesDetailView.as_view(), name='employee')
]
