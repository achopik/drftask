from rest_framework.serializers import ModelSerializer

from bookapi.models import Book


class BookListSerializer(ModelSerializer):
    """
    Serializer that shows short info about a Book instance
    """

    class Meta:
        model = Book
        fields = ['id', 'title', 'author_name']


class AdvancedBookSerializer(ModelSerializer):
    """
    Serializer that shows full info about a Book instance
    """

    class Meta:
        model = Book
        fields = ['id', 'title', 'author_name', 'description']
