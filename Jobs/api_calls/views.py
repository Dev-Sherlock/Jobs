from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.shortcuts import render
from django.views.decorators.cache import cache_page
from .models import Job
from django.views.generic.edit import FormView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

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



class JobCreate(CreateView):
    model = Job
    fields = ['title','description','author']
    template_name = 'api_calls/job_create.html'
    success_url = reverse_lazy('index')


class JobUpdate(UpdateView):
    model = Job
    fields = ['title','description','author']
    template_name = 'api_calls/job_update.html'
    success_url = reverse_lazy('index')

class JobDelete(DeleteView):
    model = Job
    context_object_name = 'task'
    success_url = reverse_lazy('index')


class ContactFormView(FormView):
    template_name = 'job_update.html'
    form_class = Job
    success_url = reverse_lazy('index')
