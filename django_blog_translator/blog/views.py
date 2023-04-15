from django.shortcuts import render
from .models import Post

# Create your views here.

class BlogView:
    model = Post
    template_name = 'blog.html'