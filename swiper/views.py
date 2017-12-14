from django.shortcuts import render
from .models import Restaurant
from django.contrib.auth import login, authenticate, get_user
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect, render_to_response
from django.template import RequestContext

from swiper.forms import MatchRestaurantForm, RemoveRestaurantForm, SignUpForm, UpdateProfile
from swiper.models import Deny, DenyManager, Match, MatchManager

@login_required
def index(request):
    """
    View function for home page of site.
    """
    restaurants = None

    if request.method == 'POST':
        add = MatchRestaurantForm(request.POST)
        if add.is_valid():
            add.save(request.user)
            return redirect('index')
    else:
        add = MatchRestaurantForm()

    user_pk = request.user.pk
    if Restaurant.objects.all():
        for rest in  Restaurant.objects.all():
            if not MatchManager.check_match(user=user_pk, restaurant=rest) and not DenyManager.check_deny(user=user_pk, restaurant=rest):
                restaurants = rest
                break
        print(restaurants)

    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={'restaurant': restaurants},
    )

@login_required
def remove_restaurant(request):
    """ function to remove the restaurant to for the current user"""
    if request.method == 'POST':
        remove = RemoveRestaurantForm(request.POST)
        if remove.is_valid():
            remove.save(request.user)
            return redirect('index')
    else:
        remove = RemoveRestaurantForm()
    return redirect('index')

@login_required
def show_restaurant(request, restaurant_id):
    """ display specific restaurant from uuid """
    try:
        restaurant = get_object_or_404(Restaurant, id=restaurant_id)
        # Render the HTML template index.html with the data in the context variable
        return render(
            request,
            'restaurant.html',
            context={'restaurant': restaurant},
        )
    except ValueError:
        raise Http404

def signup(request):
    """ the page for registration on GoudaTime """
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def profile(request):
    """
    View function for profile page of each user.
    """

    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'profile.html',
        context={},
    )

def update_profile(request):
    args = {}

    if request.method == 'POST':
        form = UpdateProfile(request.POST)
        if form.is_valid():
            form.save(request.user)
            return redirect('Profile')
    else:
        form = UpdateProfile()
    return render(request, 'profile.html', args)

@login_required
def matches(request):
    """
    View function for matches page of each user to display matched restaurants
    """
    user_pk = request.user.pk
    matches = MatchManager.get_matches(user=user_pk)

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'matches.html',
                              {'matches': matches},)


@login_required
def add_match(request):
    """
    View function for adding a match to a user
    """

    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'add_match.html',
        context={},
    )

def about(request):
    """
    View function for about page of GoudaTime.
    """

    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'about.html',
        context={},
    )

def thank_you(request):
    """
    View function for thank you page of GoudaTime.
    """

    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'registration/thank_you.html',
        context={},
    )
