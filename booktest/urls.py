# from django.conf.urls import url
from django.urls import path, re_path
from booktest import views

urlpatterns = [
    path('', views.index),
    re_path('(\d+)/', views.detail)
]
