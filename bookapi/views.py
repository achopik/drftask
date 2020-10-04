from bookapi.serializers import *

from rest_framework import viewsets


class BookViewSet(viewsets.mixins.ListModelMixin,
                  viewsets.mixins.CreateModelMixin,
                  viewsets.mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    """
    API-endpoint for all needed actions with Book model
    """
    queryset = Book.objects.all()
    lookup_field = 'id'

    def get_serializer_class(self):
        if self.action == 'list':
            return BookListSerializer
        else:
            return AdvancedBookSerializer

    def get(self, request, id=None):
        if id:
            return self.retrieve(request, id)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)


