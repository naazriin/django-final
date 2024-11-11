from django.http import JsonResponse
from position.models import Position
from position.api.serializers import PositionSerializer
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser


@api_view(['GET', 'POST'])
def position_view(request):
   position_list = Position.objects.all()
   if request.method == 'POST':
      serializer = PositionSerializer(data=request.data)
      if serializer.is_valid():
         serializer.save()
         return JsonResponse(serializer.data, safe =False,status=201)
      return JsonResponse(serializer.errors,safe=False,status=403)
         
   serializer = PositionSerializer(position_list,many=True,context = {'request': request})
   return JsonResponse(serializer.data, safe=False, json_dumps_params={'indent': 2},status=200)

class PositionListCreateApiView(ListCreateAPIView):
   serializer_class = PositionSerializer
   queryset = Position.objects.all()
   allowed_methods = ['GET','POST']
   
   
   
@api_view(['PUT', 'PATCH'])
def position_update(request,pk):
   position = Position.objects.get(id=pk)
   
   if request.method == 'PUT':
      serializer = PositionSerializer(data = request.data,instance=position)
      if serializer.is_valid():
         serializer.save()
         return JsonResponse(serializer.data, safe =False,status=201)
      return JsonResponse(serializer.errors,safe=False,status=403)
   
   elif request.method == 'PATCH':
      serializer = PositionSerializer(data = request.data,instance=position,partial=True)
      if serializer.is_valid():
         serializer.save()
         return JsonResponse(serializer.data, safe =False,status=201)
      return JsonResponse(serializer.errors,safe=False,status=403)
   
   return JsonResponse(serializer.data, safe=False, json_dumps_params={'indent': 2},status=200)


class PositionRetrieveUpdateView(RetrieveUpdateDestroyAPIView):
   serializer_class = PositionSerializer
   queryset = Position.objects.all()
   # permission_classes = [IsAuthenticated]
   
   
   
   def delete(self, request, *args, **kwargs):
        self.permission_classes = [IsAdminUser]  
        self.check_permissions(request) 
        return super().delete(request, *args, **kwargs)
   