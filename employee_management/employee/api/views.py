from django.http import JsonResponse
from employee.models import Employee
from employee.api.serializers import EmployeeSerializer
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser

@api_view(['GET', 'POST'])
def employee_view(request):
   employee_list = Employee.objects.all()
   if request.method == 'POST':
      serializer = EmployeeSerializer(data=request.data)
      if serializer.is_valid():
         serializer.save()
         return JsonResponse(serializer.data, safe =False,status=201)
      return JsonResponse(serializer.errors,safe=False,status=403)
         
   serializer = EmployeeSerializer(employee_list,many=True,context = {'request': request})
   return JsonResponse(serializer.data, safe=False, json_dumps_params={'indent': 2},status=200)

class EmployeeListCreateApiView(ListCreateAPIView):
   serializer_class = EmployeeSerializer
   queryset = Employee.objects.all()
   allowed_methods = ['GET','POST']
   
   
@api_view(['PUT', 'PATCH'])
def employee_update(request,pk):
   department = Employee.objects.get(id=pk)
   
   if request.method == 'PUT':
      serializer = EmployeeSerializer(data = request.data,instance=department)
      if serializer.is_valid():
         serializer.save()
         return JsonResponse(serializer.data, safe =False,status=201)
      return JsonResponse(serializer.errors,safe=False,status=403)
   
   elif request.method == 'PATCH':
      serializer = EmployeeSerializer(data = request.data,instance=department,partial=True)
      if serializer.is_valid():
         serializer.save()
         return JsonResponse(serializer.data, safe =False,status=201)
      return JsonResponse(serializer.errors,safe=False,status=403)
   
   return JsonResponse(serializer.data, safe=False, json_dumps_params={'indent': 2},status=200)


class EmployeeRetrieveUpdateView(RetrieveUpdateDestroyAPIView):
   serializer_class = EmployeeSerializer
   queryset = Employee.objects.all()
   # permission_classes = [IsAuthenticated]
   
   
   
   def delete(self, request, *args, **kwargs):
        self.permission_classes = [IsAdminUser]  
        self.check_permissions(request) 
        return super().delete(request, *args, **kwargs)