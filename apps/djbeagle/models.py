from django.db import models
from django.contrib.auth.models import User


class Search(models.Model):
    name        = models.CharField(max_length=128)
    criteria    = models.ManyToManyField("Criterion", blank=True)
    date        = models.DateTimeField(auto_now_add=True)
    user        = models.ForeignKey(User)
    articles    = models.ManyToManyField("Article", blank=True)
    engines     = models.ManyToManyField("Engine", blank=True)

class Criterion(models.Model):
    search_string = models.CharField(max_length=128, unique=True)

    class Meta:
        verbose_name_plural = "criteria"

class Article(models.Model):
    title       = models.TextField()
    link        = models.URLField(blank=True)
    year        = models.TextField(blank=True)
    authors     = models.TextField(blank=True)
    publication = models.CharField(max_length=128, blank=True)
    engine      = models.ForeignKey("Engine")

class Engine(models.Model):
    name        = models.CharField(max_length=128, unique=True)
