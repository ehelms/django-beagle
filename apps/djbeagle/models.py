from django.db import models
from django.contrib.auth.models import User


class Search(models.Model):
    name        = models.CharField(max_length=128)
    criteria    = models.ManyToManyField("Criterion", blank=True)
    date        = models.DateTimeField(auto_now_add=True)
    user        = models.ForeignKey(User)
    articles    = models.ManyToManyField("Article", blank=True)
    engines     = models.ManyToManyField("Engine", blank=True)
    combined    = models.ForeignKey("CombinedSearch", null=True, unique=True, on_delete=models.SET_NULL)

class CombinedSearch(models.Model):
    pass

class CombinedArticle(models.Model):
    references  = models.ManyToManyField('Article')
    search      = models.ForeignKey('CombinedSearch', related_name="combined_article")
    title       = models.TextField()

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
    criteria    = models.ManyToManyField("Criterion", blank=True)

class Engine(models.Model):
    name        = models.CharField(max_length=128, unique=True)
