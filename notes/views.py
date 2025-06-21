from rest_framework import viewsets
from rest_framework.permissions import SAFE_METHODS, BasePermission
from .models import Note
from .serializers import NoteSerializer

class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user and request.user.is_staff

class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [IsAdminOrReadOnly]
