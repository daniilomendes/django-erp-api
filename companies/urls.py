from django.urls import path
from companies.views.employees import Employees, EmployeeDetail

urlpatterns = [
    # Employees Endpoints
    path('employees', Employees.as_view()),
    path('employees/<int:employee_id>', EmployeeDetail.as_view()),

    
]