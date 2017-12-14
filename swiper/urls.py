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
    url(r'^thank-you/$', views.thank_you, name='Thank You'),
    url(r'^restaurants/(?P<restaurant_id>[0-9a-f-]+)', views.show_restaurant, name="Restaurant"),
    url(r'^remove-restaurant/$', views.remove_restaurant, name='Remove Restaurant'),
    url(r'^update-profile/$', views.update_profile, name='Update Profile'),
]
