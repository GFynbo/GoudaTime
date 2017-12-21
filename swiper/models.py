import uuid

from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from django.core.files.storage import Storage
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

# GoudaTime models!

class UserProfile(models.Model):
    """
    Model with OneToOne field for extending the default users
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    location_lat = models.DecimalField(max_digits=9, decimal_places=6, default=42.3601)
    location_lon = models.DecimalField(max_digits=9, decimal_places=6, default=-71.0589)
    address = models.CharField(max_length=125, default="Boston, MA", help_text='123 Sample St, City ST 90210')


def create_profile(sender, **kwargs):
    user = kwargs["instance"]
    if kwargs["created"]:
        user_profile = UserProfile(user=user)
        user_profile.save()
post_save.connect(create_profile, sender=User)

class Picture(models.Model):
    """
    Model to hold multiple pictures for a restaurant.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, help_text="Enter the picture name (e.g. Seating Area, or Kitchen)")
    image = models.ImageField(upload_to = 'swiper/static/img/', default = 'swiper/static/img/no-img.png')

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name

class Restaurant(models.Model):
    """
    This model stores the required information pertaining to the restaurant
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, help_text="Enter the restaurant name (e.g. Santarpio's or Jimmy's Subs)")
    description = models.TextField(max_length=1000, default="A generic restaurant.", help_text="Enter a brief description of the restaurant")
    address = models.TextField(max_length=125, default="Boston, MA", help_text='123 Sample St, City ST 90210')
    location_lat = models.DecimalField(max_digits=9, decimal_places=6, default=40.7128)
    location_lon = models.DecimalField(max_digits=9, decimal_places=6, default=-74.0060)
    hours = models.CharField(max_length=200, help_text="Enter the restaurant hours (e.g. M-F 9-5, Sat 12-5, Sun Closed)")
    pictures = models.ManyToManyField(Picture, help_text="Select pictures for this restaurant")
    category = models.CharField(max_length=50, help_text="Enter the general food category (e.g. Mexican, American, Thai, etc)")

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return str(self.name)


class MatchManager(models.Manager):
    """
    This is the manager class for the match system for creating users and helpful
    functions in general.
    """
    def total_matches():
        matches = Match.objects.all()
        return len(matches)

    def get_matches(user, deny=False):
        # get matches for the match page
        matches = Match.objects.filter(user=user, deny=deny)
        return matches

    def check_match(user, restaurant):
        return Match.objects.filter(user=user, restaurant=restaurant)

    def add_match(user, restaurant, deny=False):
        new_match = Match(user=user, restaurant=restaurant, deny=deny)
        new_match.save()

class Match(models.Model):
    """
    A match is a bi-directional association between a restaurant and user who
    wants the association (match).
    """
    user = models.ForeignKey(User, related_name="match_user")
    restaurant = models.ForeignKey(Restaurant, related_name="match_restaurant")
    date_matched = models.DateField(auto_now_add=True, editable=False)
    deny = models.BooleanField(default=False)
