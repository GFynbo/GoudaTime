from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from django.core.files.storage import Storage
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Picture(models.Model):
    """
    Model to hold multiple pictures for a restaurant.
    """
    name = models.CharField(max_length=100, help_text="Enter the picture name (e.g. Seating Area, or Kitchen)")
    image = models.ImageField(upload_to = 'swiper/static/img/' + str(datetime.utcnow()), default = 'swiper/static/img/no-img.png')

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name

class Restaurant(models.Model):
    """
    This model stores the required information pertaining to the restaurant
    """

    name = models.CharField(max_length=100, help_text="Enter the restaurant name (e.g. Santarpio's or Jimmy's Subs)")
    manager = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

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
    profile_pic = models.ImageField(upload_to = 'swiper/static/img/' + str(User.username), default = 'swiper/static/img/no-img.png')
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    matches = models.ManyToManyField(Restaurant, help_text="List of matches for each user to a restaurant.")
    current_location_x = models.DecimalField(max_digits=9, decimal_places=6, default=42.3601)
    current_location_y = models.DecimalField(max_digits=9, decimal_places=6, default=71.0589)

    def add_restaurant_to_matches(self, restaurant):
        ''' add a selected restaurant to the user '''
        if (restaurant not in self.matches):
            self.matches.add(restaurant)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
