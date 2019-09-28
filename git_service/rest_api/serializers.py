from rest_framework import serializers

from . import models


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AuthorModel
        exclude = ()


class RepoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.RepoModel
        exclude = ()


class GitEventSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    repo = RepoSerializer()

    class Meta:
        model = models.GitEventModel
        exclude = ()

    def create(self, validated_data):
        author_data = validated_data.pop('author_data')
        repo_data = validated_data.pop('repo_data')


        author = models.AuthorModel.objects