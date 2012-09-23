from django.contrib import admin
from djbeagle.models import Search, Article, Engine, Criterion, CombinedSearch, CombinedArticle

admin.site.register(Search)
admin.site.register(Article)
admin.site.register(Engine)
admin.site.register(Criterion)
admin.site.register(CombinedSearch)
admin.site.register(CombinedArticle)
