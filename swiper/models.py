import uuid

from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from django.core.files.storage import Storage
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

# Create your models here.
class Picture(models.Model):
    """
    Model to hold multiple pictures for a restaurant.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, help_text="Enter the picture name (e.g. Seating Area, or Kitchen)")
    image = models.ImageField(upload_to = 'swiper/static/img/' + str(id), default = 'swiper/static/img/no-img.png')

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

    description = models.TextField(max_length=1000, help_text="Enter a brief description of the restaurant")
    address = models.CharField(max_length=75, help_text='123 Sample St, City ST 90210')

    hours = models.CharField(max_length=200, help_text="Enter the restaurant hours (e.g. M-F 9-5, Sat 12-5, Sun Closed)")
    pictures = models.ManyToManyField(Picture, help_text="Select pictures for this restaurant")

    category = models.CharField(max_length=50, help_text="Enter the general food category (e.g. Mexican, American, Thai, etc)")

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name

class Profile(models.Model):
    """
    Extension of the User model to allow some extra information
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to = 'swiper/static/img/' + str(timezone.now), default = 'swiper/static/img/no-img.png')
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def get_matches(self):
        matches = Match.objects.filter(user=self.user)
        return matches

    def add_match(self, restaurant):
        new_match = Match(user=self.user, restaurant=restaurant, date_matched=timezone.now)
        new_match.save()

class Match(models.Model):
    """
    A match is a bi-directional association between a restaurant and user who
    wants the association (match).
    """
    user = models.ForeignKey(User, related_name="match_user")
    restaurant = models.ForeignKey(Restaurant, related_name="match_restaurant")
    date_matched = models.DateField(default=timezone.now, editable=False)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
