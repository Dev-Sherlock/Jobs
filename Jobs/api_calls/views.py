from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.shortcuts import render
from django.views.decorators.cache import cache_page
from .models import Job
from django.views.generic import TemplateView, ListView


CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


@cache_page(CACHE_TTL)
def index(request):
    if request.method=='GET':
        jobs=Job.objects.all()
    else:
        jobs=Job.objects.filter(title__icontains='title')#STILL DOESN"T WORK

    context={'jobs': jobs}
    return render(request, 'api_calls/index.html',context)


@cache_page(CACHE_TTL)
def post(request,id):
    job=Job.objects.get(id=id)
    context={'job': job}
    return render(request, 'api_calls/post.html',context)

