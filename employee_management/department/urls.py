from django.urls import path

from department.views import department

urlpatterns = [
    path("",department,name="department_page"),
]