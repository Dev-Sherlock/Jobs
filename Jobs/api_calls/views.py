# from django.shortcuts import render
# from .services import get_recipes
#
#
# def recipes_view(request):
#     return render(request, 'api_calls/index.html', {
#         'recipes': get_recipes()
#     })


from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.shortcuts import render
from django.views.decorators.cache import cache_page
from .models import Job

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


@cache_page(CACHE_TTL)
def index(request):
    jobs=Job.objects.all()
    context={'jobs': jobs}
    return render(request, 'api_calls/index.html',context)


@cache_page(CACHE_TTL)
def post(request,id):
    job=Job.objects.get(id=id)
    context={'job': job}
    return render(request, 'api_calls/post.html',context)
