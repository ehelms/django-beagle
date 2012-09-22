from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.conf import settings
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required

from djbeagle.forms import SearchForm
from djbeagle.models import Search, Article
from djbeagle.lib.engines import util
from djbeagle.lib.search import run
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
def search(request):
    if request.method == "POST":
        search = Search(user=request.user)
        search_form = SearchForm(request.POST, instance=search)
        if search_form.is_valid():
            saved_search = search_form.save()
            results = run([request.POST['engine']], request.POST['criteria'])
            for result in results:
                saved_search.article.get_or_create(title=result['title'])
            return render_to_response("djbeagle/results.html",
                            { 'article_list' : results },
                            context_instance=RequestContext(request))
        else:
            return HttpResponse("fail")
