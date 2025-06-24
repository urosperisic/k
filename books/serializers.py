from rest_framework import serializers
from .models import Author, Book

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

# class BookSerializer(serializers.ModelSerializer):
#     authors = AuthorSerializer(many=True, read_only=True)
#     author_ids = serializers.PrimaryKeyRelatedField(
#         many=True, write_only=True, queryset=Author.objects.all(), source='authors'
#     )

#     class Meta:
#         model = Book
#         fields = ['id', 'title', 'authors', 'author_ids']

class BookSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True, read_only=True)
    author_ids = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Author.objects.all(), write_only=True, required=False
    )
    new_authors = AuthorSerializer(many=True, write_only=True, required=False)

    class Meta:
        model = Book
        fields = ['id', 'title', 'authors', 'author_ids', 'new_authors']

    def validate(self, data):
        author_ids = data.get('author_ids', [])
        new_authors = data.get('new_authors', [])
        new_author_names = {a['name'].strip().lower() for a in new_authors}
        existing_author_names = {a.name.strip().lower() for a in author_ids}
        conflict = new_author_names & existing_author_names
        if conflict:
            raise serializers.ValidationError(
                f"The following author(s) already exist: {', '.join(conflict)}"
            )
        return data

    def create(self, validated_data):
        author_ids = validated_data.pop('author_ids', [])
        new_authors = validated_data.pop('new_authors', [])
        book = Book.objects.create(**validated_data)
        for author in author_ids:
            book.authors.add(author)
        for author_data in new_authors:
            author, created = Author.objects.get_or_create(**author_data)
            book.authors.add(author)
        return book

    def update(self, instance, validated_data):
        author_ids = validated_data.pop('author_ids', [])
        new_authors = validated_data.pop('new_authors', [])
        instance.title = validated_data.get('title', instance.title)
        instance.save()
        if author_ids or new_authors:
            instance.authors.clear()
            for author in author_ids:
                instance.authors.add(author)
            for author_data in new_authors:
                author, created = Author.objects.get_or_create(**author_data)
                instance.authors.add(author)
        return instance
