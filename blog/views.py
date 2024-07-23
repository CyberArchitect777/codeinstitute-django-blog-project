from django.views import generic
from .models import Post
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

class PostList(generic.ListView):
    #queryset = Post.objects.all()
    #queryset = Post.objects.filter(author=2) # Filtering by the author ID of 2    
    #Post.objects.all().order_by("-created_on")
    queryset = Post.objects.filter(status=1)
    template_name = "blog/index.html"
    paginate_by = 6
