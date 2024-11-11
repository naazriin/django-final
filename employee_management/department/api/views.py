from django.http import JsonResponse
from department.models import Department
from department.api.serializers import DepartmentSerializer
from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser


@api_view(['GET', 'POST'])
def department_view(request):
   department_list = Department.objects.all()
   if request.method == 'POST':
      serializer = DepartmentSerializer(data=request.data)
      if serializer.is_valid():
         serializer.save()
         return JsonResponse(serializer.data, safe =False,status=201)
      return JsonResponse(serializer.errors,safe=False,status=403)
         
   serializer = DepartmentSerializer(department_list,many=True,context = {'request': request})
   return JsonResponse(serializer.data, safe=False, json_dumps_params={'indent': 2},status=200)

class DepartmentListCreateApiView(ListCreateAPIView):
   serializer_class = DepartmentSerializer
   queryset = Department.objects.all()
   allowed_methods = ['GET','POST']
   
   # def  get_serializer_class(self):
   #    if self.request.method == 'POST':
   #       self.serializer_class = DepartmentSerializer 
   #    return self.serializer_class

@api_view(['PUT', 'PATCH'])
def department_update(request,pk):
   department = Department.objects.get(id=pk)
   
   if request.method == 'PUT':
      serializer = DepartmentSerializer(data = request.data,instance=department)
      if serializer.is_valid():
         serializer.save()
         return JsonResponse(serializer.data, safe =False,status=201)
      return JsonResponse(serializer.errors,safe=False,status=403)
   
   elif request.method == 'PATCH':
      serializer = DepartmentSerializer(data = request.data,instance=department,partial=True)
      if serializer.is_valid():
         serializer.save()
         return JsonResponse(serializer.data, safe =False,status=201)
      return JsonResponse(serializer.errors,safe=False,status=403)
   
   return JsonResponse(serializer.data, safe=False, json_dumps_params={'indent': 2},status=200)


class DepartmentRetrieveUpdateView(RetrieveUpdateDestroyAPIView):
   serializer_class = DepartmentSerializer
   queryset = Department.objects.all()
   # permission_classes = [IsAuthenticated]
   
   
   
   def delete(self, request, *args, **kwargs):
        self.permission_classes = [IsAdminUser]  
        self.check_permissions(request) 
        return super().delete(request, *args, **kwargs)
   
