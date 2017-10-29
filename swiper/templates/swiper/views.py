from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    """
    View function for home page of site.
    """
    # Available books (status = 'a')

    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={},
    )
