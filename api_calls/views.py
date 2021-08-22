from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.shortcuts import render, redirect
from django.views.decorators.cache import cache_page
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

from .models import Job
from .serializers import JobSerializer
from rest_framework import generics


class JobList(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer


class JobDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer


# @cache_page(CACHE_TTL)
def index(request):
    if request.method == 'GET':
        jobs = Job.objects.all()
    else:
        query = request.POST['query']
        jobs = Job.objects.filter(title__icontains=query)

    context = {'jobs': jobs}
    return render(request, 'api_calls/index.html', context)


@cache_page(CACHE_TTL)
def post(request, id):
    job = Job.objects.get(id=id)
    context = {'job': job}
    return render(request, 'api_calls/post.html', context)


class JobCreate(CreateView):
    model = Job
    fields = ['title', 'description']
    template_name = 'api_calls/job_create.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(JobCreate, self).form_valid(form)


class JobUpdate(UpdateView):
    model = Job
    fields = ['title', 'description']
    template_name = 'api_calls/job_update.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(JobUpdate, self).form_valid(form)


class JobDelete(DeleteView):
    model = Job
    context_object_name = 'task'
    success_url = reverse_lazy('index')


def signup(request):
    if request.user.is_authenticated:
        return redirect('index', username=request.user.username)

    if request.method == 'POST':
        f = UserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            return redirect('login')
    else:
        f = UserCreationForm()

    return render(request, 'api_calls/signup.html', {'form': f})
