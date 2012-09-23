from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.conf import settings
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.utils import simplejson as json

from djbeagle.forms import SearchForm
from djbeagle.models import Search, Article, Engine, Criterion, CombinedSearch, CombinedArticle
from djbeagle.lib.engines import util
from djbeagle.lib.search import run
#from djbeagle.lib import combine
#from djbeagle.lib import document

@login_required
def home(request):
    search_form = SearchForm()
    engine_list = util.get_engine_titles()
    return render_to_response("djbeagle/home.html",
                { "search_form" : search_form,
                 'engine_list' : engine_list, },
                context_instance=RequestContext(request))


@login_required
def search(request, search_id=None):
    if request.method == "POST":
        search = Search(user=request.user)
        search_form = SearchForm(request.POST, instance=search)
        if search_form.is_valid():
            saved_search = search_form.save()

            for criterion in request.POST.getlist('criterion'):
                saved_search.criteria.add(Criterion.objects.get_or_create(search_string=criterion)[0])

                for engine in request.POST.getlist('engine'):
                    engine_obj = Engine.objects.get_or_create(name=engine)[0]
                    saved_search.engines.add(engine_obj)
                    results = run(engine, criterion)

                    for result in results:
                        article = Article.objects.get_or_create(title=result['title'], year=result['year'], 
                                                            link=result['link'], authors=result['authors'],
                                                            engine=engine_obj)[0]
                        article.criteria.add(Criterion.objects.get_or_create(search_string=criterion)[0])
                        saved_search.articles.add(article)

            return redirect('search_url', search_id=saved_search.id)
        else:
            return HttpResponse("fail")
    elif request.method == "GET":
        if search_id is None:
            search_list = Search.objects.all()
            search_form = SearchForm()
            engine_list = util.get_engine_titles()

            return render_to_response("djbeagle/home.html",
                        {"search_form"  : search_form,
                        "engine_list"   : engine_list,
                        "search_list"   : search_list},
                        context_instance=RequestContext(request))
        else:
            search = Search.objects.get(pk=search_id)
            return render_to_response("djbeagle/search.html",
                        {'search' : search},
                        context_instance=RequestContext(request))
    elif request.method == 'DELETE':
        search = Search.objects.get(pk=search_id)
        try:
            search.delete()
            response = { 'status' : 'success' }
        except:
            response = { 'status' : 'error' }

        return HttpResponse(json.dumps(response), mimetype="application/json")

def combined_search(request, search_id):
    if request.method == 'POST':
        search = Search.objects.get(pk=search_id)
        combined = CombinedSearch()
        combined.save()
        search.combined = combined
        search.save()

        articles = {}

        for article in search.articles.all():
            if article.title in articles:
                articles[article.title]['references'].append(article)
            else:
                articles[article.title] = { 'title' : article.title, 'references' : [article] }

        for key,value in articles.iteritems():
            combined_article = CombinedArticle(title=value['title'], search=combined)
            combined_article.save()
        
            for reference in value['references']:
                combined_article.references.add(reference)

        return redirect('search_url', search_id=search.id)
