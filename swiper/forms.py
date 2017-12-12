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
        MatchManager.add_match(user=curr_user, restaurant=restaurant)

    #  # Overriding save allows us to process the value of 'toppings' field
    # def save(self, commit=True):
    #     # Get the unsave Pizza instance
    #     instance = forms.ModelForm.save(self, False)
    #
    #     # Prepare a 'save_m2m' method for the form,
    #     old_save_m2m = self.save_m2m
    #     def save_m2m():
    #        old_save_m2m()
    #        # This is where we actually link the pizza with toppings
    #        instance.topping_set.clear()
    #        for topping in self.cleaned_data['toppings']:
    #            instance.topping_set.add(topping)
    #     self.save_m2m = save_m2m
    #
    #     # Do we need to save all changes now?
    #     if commit:
    #         instance.save()
    #         self.save_m2m()
    #
    #     return instance
