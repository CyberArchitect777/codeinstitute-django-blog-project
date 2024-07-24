from django.shortcuts import render
from .models import About
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.

queryset = Post.objects.first()
about = get_object_or_404(queryset)

return render(
    request,
    "about/about.html",
    { "about": about }
)
