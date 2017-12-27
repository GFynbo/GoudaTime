from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save


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
