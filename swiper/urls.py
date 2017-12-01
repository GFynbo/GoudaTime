from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.conf.urls import include


from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^profile/', views.profile, name="Profile"),
    url(r'^about/', views.about, name="About"),
    url(r'^matches/', views.matches, name="Matches"),
    url(r'^(?P<restaurant_name>\d+)/', views.add_match, name="Add Match"),
    url(r'^signup/$', views.signup, name='Signup'),
]
