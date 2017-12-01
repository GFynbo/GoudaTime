from django.shortcuts import render
from .models import Restaurant
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

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

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
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
