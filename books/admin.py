from django.contrib import admin
from .models import Author, Book

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'get_authors']
    search_fields = ['title', 'authors__name']

    def get_authors(self, obj):
        return ", ".join([a.name for a in obj.authors.all()])
    get_authors.short_description = "Authors"
