from rest_framework.serializers import ModelSerializer

from bookapi.models import Book


class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author_name']


class AdvancedBookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author_name', 'description']



