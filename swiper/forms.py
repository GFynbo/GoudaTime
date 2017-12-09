from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from swiper.models import Profile

class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', )

class AddRestaurantForm(forms.ModelForm):
    restaurant_name = forms.CharField(max_length=100, help_text="Enter the restaurant name (e.g. Santarpio's or Jimmy's Subs)")

    class Meta:
        model = Profile
        fields = ('matches', )
