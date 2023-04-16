from django.shortcuts import render
from .models import Post
from django.views import generic

# Create your views here.
class BlogView(generic.DetailView):
    model = Post
    template_name = 'blog.html'
    

class HomeView(generic.TemplateView):
    template_name = 'index.html'