from bookapi.serializers import *

from django.shortcuts import render

from rest_framework import generics



class BookList(generics.ListAPIView):
    """
    GET-request: show the list of books
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class CreateBook(generics.CreateAPIView):
    """
    POST-request: create a new book
    """
    queryset = Book.objects.all()
    serializer_class = AdvancedBookSerializer


class BookDetail(generics.RetrieveAPIView):
    """
    GET-request: get detailed info about book by ID
    """
    queryset = Book.objects.all()
    serializer_class = AdvancedBookSerializer
