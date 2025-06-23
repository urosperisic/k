from rest_framework import permissions

class IsAdminOrReadPostOnly(permissions.BasePermission):
    """
    Admin: Full access.
    Authenticated user: can GET and POST.
    """
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if request.user.role == 'admin':
                return True  # full access
            elif request.method in ['GET', 'POST']:
                return True  # limited access
        return False  # not authenticated

    def has_object_permission(self, request, view, obj):
        if request.user.role == 'admin':
            return True
        elif request.user.role == 'user':
            return request.method in ['GET']
        return False