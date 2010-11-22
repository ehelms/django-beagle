from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.conf import settings
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required

from djbeagle.forms import SearchForm
from djbeagle.models import Search

@login_required
def home(request):
    search_form = SearchForm()
    return render_to_response("djbeagle/home.html",
                { "search_form" : search_form, },
                context_instance=RequestContext(request))


@login_required
def search(request):
    if request.METHOD == "POST":
        search = Search(user=request.username)
        search_form = SearchForm(instance=search)
        if search_form.is_valid():
            search_form.save()
            return HttpResponse("success")
