import uuid

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
    profile_pic = models.ImageField(upload_to = 'swiper/static/img/' + str(User.username), default = 'swiper/static/img/no-img.png')
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def add_restaurant_to_matches(self, restaurant):
        ''' add a selected restaurant to the user '''
        if (restaurant not in self.matches):
            self.matches.add(restaurant)

class MatchManager(models.Manager):

    def matches_for_user(self, user):
        matches = []
        for match in self.filter(from_user=user).select_related(depth=1):
            matches.append({"match": match.to_restaurant, "match": match})
        return friends

    def are_matched(self, user, restaurant):
        if self.filter(user=user, restaurant=restaurant).count() > 0:
            return True
        return False

    def remove(self, user, restaurant):
        if self.filter(to_user=user):
            friendship = self.filter(to_user=user, match)
        match.delete()

class Match(models.Model):
    """
    A match is a uni-directional association between a restaurant and user who
    wants the association (match).
    """
    if not Match.objects.are_matched(self.user, self.restaurant):
            friendship = Match(user=self.user, restaurant=self.restaurant)
            friendship.save()
            self.status = "5"
            self.save()
            if notification:
                notification.send([self.from_user], "friends_accept", {"invitation": self})
                notification.send([self.to_user], "friends_accept_sent", {"invitation": self})
                for user in friend_set_for(self.to_user) | friend_set_for(self.from_user):
                    if user != self.to_user and user != self.from_user:
                        notification.send([user], "friends_otherconnect", {"invitation": self, "to_user": self.to_user})

    to_restaurant = models.ForeignKey(User, related_name="matches")
    # @@@ relationship types
    added = models.DateField(default=datetime.date.today)

    objects = MatchManager()

    class Meta:
        unique_together = ('to_restaurant',)

def match_set_for(user):
    return set([obj["match"] for obj in Match.objects.matches_for_user(user)])

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
