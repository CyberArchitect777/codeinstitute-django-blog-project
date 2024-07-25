from django.shortcuts import render
from .models import About
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.

def about_me(request):
    """
    Renders the About page
    """
    queryset = About.objects.first()
    #about = get_object_or_404(queryset, request)
    about = About.objects.all().order_by('-updated_on').first()

    return render(
        request,
        "about/about.html",
        { "about": about },
    )