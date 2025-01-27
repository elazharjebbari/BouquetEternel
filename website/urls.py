from django.urls import path

from website.views import views_home

urlpatterns = [
    path('', views_home, name='views_home'),
    path('home', views_home, name='views_homepage'),
]
