import uuid

from datetime import datetime

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class GroupManager(models.Manager):
    """
    This is the manager class for the group/friend system for creating groups and helpful
    functions in general.
    """
    def total_groups():
        groups = Group.objects.all()
        return len(groups)

    def get_group(user, deny=False):
        # get matches for the match page
        if user.has_group:
            group = Group.objects.get(user_one=user)
            return group
        else:
            return None

    def check_group(user):
        return user.has_group

    def make_group(user_one, user_two, user_three, user_four):
        new_group = Group(user_one=user_one, user_two=user_two, user_three=user_three, user_four=user_four)
        new_group.save()

    def find_friend(username):
        return User.objects.get(username=username)

class Group(models.Model):
    """
    A group is a multi-directional association between two to four users for the
    group functionality.
    """
    user_one = models.ForeignKey(User, related_name="group_user_one")
    user_two = models.ForeignKey(User, related_name="group_user_two")
    user_three = models.ForeignKey(User, related_name="group_user_three")
    user_four = models.ForeignKey(User, related_name="group_user_four")
