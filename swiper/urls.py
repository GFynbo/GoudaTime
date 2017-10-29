from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.conf.urls import include


from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^accounts/', include('django.contrib.auth.urls')),
]
