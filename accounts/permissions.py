from rest_framework import permissions

class IsAuthor(permissions.BasePermission):
    '''
    API permissions for the authenticated users.

    They can view the lists but they can update only order and repair that they created.
    '''
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if obj.author == request.user:
            return True
        return False

class IsSuper(permissions.BasePermission):
    '''
    API permissions for the superuser users.

    '''
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True
        return False