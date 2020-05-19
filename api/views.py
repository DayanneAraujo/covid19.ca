from .serializers import *
from rest_framework import viewsets, status
from rest_framework.response import Response

class CanadaViewSet(viewsets.ModelViewSet):
    queryset = Covid19Ca.objects.all()
    serializer_class = CanadaSerializer
    filter_fields = ('prname',)

    def create(self, request, *args, **kwargs):
        response = {'message': 'You are not allowed to insert data.'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        response = {'message': 'You are not allowed to delete content.'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        response = {'message': 'You are not allowed to update.' }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, *args, **kwargs):
        response = {'message': 'You are not allowed to update.'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
