from rest_framework import permissions

class IsAdminUserForDelete(permissions.BasePermission):


    def has_permission(self, request, view):
        if request.method == 'DELETE':
            return request.user.is_authenticated and request.user.is_staff
        return True  
