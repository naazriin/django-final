from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .permissions import IsAdminUserForDelete

from django.contrib.auth.decorators import user_passes_test
from django.http import JsonResponse
from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View



class ExampleDeleteView(APIView):
    permission_classes = [IsAdminUserForDelete]

    def delete(self, request, *args, **kwargs):
        return Response({"message": "Deleted!"}, status=status.HTTP_204_NO_CONTENT)


def is_admin(user):
    return user.is_authenticated and user.is_staff

@user_passes_test(is_admin)
def delete_view(request):
    if request.method == 'DELETE':
        return JsonResponse({'message': 'Deleted!'}, status=204)
    return JsonResponse({'error': 'Only the DELETE method is allowed.'}, status=405)




class ProtectedView(LoginRequiredMixin, View):
    def get(self, request):
        return JsonResponse({'message': 'This page is for logged in users only.'})
