from django.db import models
from django.contrib.auth.models import User


class Search(models.Model):
    criteria = models.CharField(max_length=128)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)
    article = models.ManyToManyField("Article", blank=True)

class Article(models.Model):
    title = models.TextField()
