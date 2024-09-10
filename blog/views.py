from django.shortcuts import render
from django.views import generic
from .models import Post

# Create your views here.
class PostList(generic.ListView):
    #model = Post

    # alternative way to code
    #queryset = Post.objects.filter(author=1).order_by("-created_on")
    queryset = Post.objects.filter(status=1) 
    #template_name = "post_list.html"