import uuid

from datetime import datetime

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from .profile import UserProfile


class GroupManager(models.Manager):
    """
    This is the manager class for the group/friend system for creating users and helpful
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

class Group(models.Model):
    """
    A match is a bi-directional association between a restaurant and user who
    wants the association (match).
    """
    user_one = models.ForeignKey(User, related_name="group_user_one")
    user_two = models.ForeignKey(User, related_name="group_user_two")
    user_three = models.ForeignKey(User, related_name="group_user_three")
    user_four = models.ForeignKey(User, related_name="group_user_four")
