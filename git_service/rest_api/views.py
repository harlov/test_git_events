from rest_framework import viewsets

from . import (
    models,
    serializers,
)


class AuthorsViewSet(viewsets.ModelViewSet):
    queryset = models.AuthorModel.objects.all()
    serializer_class = serializers.AuthorSerializer


class ReposViewSet(viewsets.ModelViewSet):
    queryset = models.RepoModel.objects.all()
    serializer_class = serializers.RepoSerializer


class EventsViewSet(viewsets.ModelViewSet):
    queryset = models.GitEventModel.objects.all()
    serializer_class = serializers.GitEventSerializer

