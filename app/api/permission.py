from rest_framework import permissions


class AppBasePermissionClass(permissions.BasePermission):
    def is_authenticated(self, request):
        return request.user and request.user.is_authenticated
    
    def is_admin(self, request):
        return request.user and request.user.is_authenticated and request.user.is_staff

    def has_permission(self, request, view):
        if view.action == 'list':  
            return True
        if view.action == 'retrieve':  
            return True
        if self.is_admin(request) and view.action == 'create':  
            return True
        if self.is_admin(request) and view.action == 'update':  
            return True
        if self.is_admin(request) and view.action == 'partial_update':  
            return True
        if self.is_admin(request) and view.action == 'destroy':
            return True

        return False