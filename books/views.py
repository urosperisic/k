# from rest_framework import viewsets
# from .models import Author, Book
# from .serializers import AuthorSerializer, BookSerializer
# from rest_framework.permissions import AllowAny

# class AuthorViewSet(viewsets.ModelViewSet):
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer
#     permission_classes = [AllowAny]

# class BookViewSet(viewsets.ModelViewSet):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     permission_classes = [AllowAny]

from rest_framework import viewsets, filters
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer
from rest_framework.permissions import AllowAny

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [AllowAny]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'authors__name']

