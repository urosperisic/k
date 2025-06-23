from rest_framework import viewsets
from .models import Note
from .serializers import NoteSerializer
from .permissions import IsAdminOrReadOnly

class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [IsAdminOrReadOnly]
