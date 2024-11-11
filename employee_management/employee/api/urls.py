from django.urls import path

from employee.api.views import (employee_view,
                                   EmployeeListCreateApiView,EmployeeRetrieveUpdateView,)

urlpatterns = [
    # path('employee/', employee_view , name='employee'),
    path('employee/', EmployeeListCreateApiView.as_view(), name='employee'),
    path('employee/<int:pk>/', EmployeeRetrieveUpdateView.as_view() , name='employee_update'),
]
