from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from swiper.models import Profile, Restaurant

class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', )

class AddRestaurantForm(forms.ModelForm):
    name = "test name"
    class Meta:
        model = Profile
        fields = ('matches', )
