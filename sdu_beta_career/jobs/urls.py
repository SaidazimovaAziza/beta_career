from django.conf.urls import url
from django.urls import path, include
from django.contrib import admin
from . import views


urlpatterns = [
    path('', views.job_list, name='job_list'),
    path('<int:pk>/', views.job_detail, name='job_detail'),
]
