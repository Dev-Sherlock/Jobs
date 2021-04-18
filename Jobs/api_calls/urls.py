from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('<int:id>/', post, name="post"),
    # path('<str:pk>/', JobDetail.as_view(), name='job'),
    path('job-create/', JobCreate.as_view(), name='job-create'),
    path('job-update/<str:pk>/', JobUpdate.as_view(), name='job-update'),
    path('job-delete/<str:pk>/', JobDelete.as_view(), name='job-delete'),
]


