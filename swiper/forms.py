from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from swiper.models import Deny, DenyManager, Match, MatchManager, Restaurant
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

        # dont add an existing match!
        if not Deny.objects.filter(user=curr_user, restaurant=restaurant):
            DenyManager.add_deny(user=curr_user, restaurant=restaurant)

class UpdateProfile(forms.ModelForm):
    username = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')

    def clean_email(self):
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')

        if email and User.objects.filter(email=email).exclude(username=username).count():
            raise forms.ValidationError('This email address is already in use. Please supply a different email address.')
        return email

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user
