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
def search(request, search_id=None):
    if request.method == "POST":
        search = Search(user=request.user)
        search_form = SearchForm(request.POST, instance=search)
        if search_form.is_valid():
            saved_search = search_form.save()
            results = run(request.POST.getlist('engine'), request.POST['criterion'])

            for criterion in request.POST.getlist('criterion'):
                saved_search.criteria.get_or_create(search_string=criterion)
            for engine in request.POST.getlist('engine'):
                saved_search.engines.get_or_create(name=engine)
            for result in results:
                saved_search.articles.get_or_create(title=result['title'], year=result['year'], 
                                                    link=result['link'], authors=result['authors'],
                                                    engine=request.POST['engine'])
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
            
