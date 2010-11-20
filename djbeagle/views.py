from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.conf import settings
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render_to_response("djbeagle/home.html",
                context_instance=RequestContext(request))
