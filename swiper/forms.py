from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from swiper.models import Match, MatchManager, Restaurant, UserProfile


class SignUpForm(UserCreationForm):
    """
    Form for registering the user in the system.
    """

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )

class MatchRestaurantForm(forms.Form):
    """
    Add a restaurant match between a user and a restaurant in a bi-directional relationship
    """
    restaurant_id = forms.UUIDField(help_text="Enter the restaurant id.", required=True)

    def save(self, user):
        curr_user = User.objects.get(pk=user.pk)
        restaurant = Restaurant.objects.get(pk=self.cleaned_data['restaurant_id'])

        # dont add an existing match!
        if not Match.objects.filter(user=curr_user, restaurant=restaurant):
            MatchManager.add_match(user=curr_user, restaurant=restaurant)

class RemoveRestaurantForm(forms.Form):
    """
    Form to add a denial between a user and a restaurant in the same bi-directional
    relationship listed above
    """
    restaurant_id = forms.UUIDField(help_text="Enter the restaurant id.", required=True)

    def save(self, user, deny=True):
        curr_user = User.objects.get(pk=user.pk)
        restaurant = Restaurant.objects.get(pk=self.cleaned_data['restaurant_id'])

        # dont add an existing match!
        if not Match.objects.filter(user=curr_user, restaurant=restaurant):
            MatchManager.add_match(user=curr_user, restaurant=restaurant, deny=deny)

class RemoveMatchForm(forms.Form):
    """
    Remove the match from the list of matches with a relationship to the user
    """
    restaurant_id = forms.UUIDField(help_text="Enter the restaurant id.", required=True)

    def save(self, user):
        curr_user = User.objects.get(pk=user.pk)
        restaurant = Restaurant.objects.get(pk=self.cleaned_data['restaurant_id'])

        # set the match to deny
        rest = Match.objects.get(user=curr_user, restaurant=restaurant)
        rest.deny = True
        rest.save()

class UpdateProfile(forms.ModelForm):
    """
    Update the information of the user and change it in the system
    """
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=False, max_length=50)
    last_name = forms.CharField(required=False, max_length=50)

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name')

    def save(self, user, commit=True):
        user = User.objects.get(pk=user.pk)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        if commit:
            user.save()

class UpdateLocation(forms.ModelForm):
    """
    Updates/sets the location of a given user on the homepage
    """
    location_lat = forms.DecimalField(required=True, max_digits=9, decimal_places=6)
    location_lon = forms.DecimalField(required=True, max_digits=9, decimal_places=6)
    address = forms.CharField(required=True, max_length=125)

    class Meta:
        model = UserProfile
        fields = ('location_lat', 'location_lon', 'address')

    def save(self, user, commit=True):
        user = User.objects.get(pk=user.pk)
        user.profile.location_lat = self.cleaned_data['location_lat']
        user.profile.location_lon = self.cleaned_data['location_lon']
        user.profile.address = self.cleaned_data['address']

        if commit:
            user.profile.save()
