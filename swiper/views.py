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
        context={'restaurants_list': Restaurant.objects.all()},
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
