from django.urls import path

from department.api.views import (department_view,department_update,
                                  DepartmentListCreateApiView,DepartmentRetrieveUpdateView,)

urlpatterns = [
    # path('department/', department_view , name='department'),
    path('department/', DepartmentListCreateApiView.as_view() , name='department'),
    # path('department/<int:pk>/', department_update , name='department_update'),
    path('department/<int:pk>/', DepartmentRetrieveUpdateView.as_view() , name='department_update'),
]