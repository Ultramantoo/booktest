# from django.conf.urls import url
from django.urls import path
from booktest import views

urlpatterns = [
    path('', views.index),
]
