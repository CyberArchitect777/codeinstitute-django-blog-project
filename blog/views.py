from django.views import generic
from .models import Post
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

class PostList(generic.ListView):
    queryset = Post.objects.all()
    template_name = "post_list.html"
