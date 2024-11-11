from django.urls import path

from employee.views import employee

urlpatterns = [
    path("",employee,name="employee_page"),
]