from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Restaurant

@login_required
def index(request):
    """
    View function for home page of site.
    """

    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={'restaurant': Restaurant.objects.all()[0]},
    )

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

@login_required
def matches(request):
    """
    View function for matches page of each user to display matched restaurants
    """

    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'matches.html',
        context={},
    )

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
