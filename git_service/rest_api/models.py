from django.db import models


class RepoModel(models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=100)


class AuthorModel(models.Model):
    name = models.CharField(max_length=100)
    avatar_url = models.URLField(max_length=255)


class GitEventModel(models.Model):
    name = models.CharField(max_length=100)
    emitted_at = models.DateTimeField()
    author = models.ForeignKey(AuthorModel, on_delete=models.DO_NOTHING)
    repo = models.ForeignKey(RepoModel, on_delete=models.DO_NOTHING)
