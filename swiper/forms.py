from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from swiper.models import Match, MatchManager, Restaurant
from django.shortcuts import get_object_or_404

class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )

class MatchRestaurantForm(forms.Form):
    restaurant_id = forms.UUIDField(help_text="Enter the restaurant id.")

    def save(self, user):
        curr_user = User.objects.get(pk=user.pk)
        restaurant = Restaurant.objects.get(pk=self.cleaned_data['restaurant_id'])

        # dont add an existing match!
        if not Match.objects.filter(user=curr_user, restaurant=restaurant):
            MatchManager.add_match(user=curr_user, restaurant=restaurant)

class RemoveRestaurantForm(forms.Form):
    restaurant_id = forms.UUIDField(help_text="Enter the restaurant id.")

    def save(self, user):
        curr_user = User.objects.get(pk=user.pk)
        restaurant = Restaurant.objects.get(pk=self.cleaned_data['restaurant_id'])

        print("made it!")
