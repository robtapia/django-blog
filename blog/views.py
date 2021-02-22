from django.shortcuts import render

from django.views.generic import ListView
from .models import Post

class BlogListView(ListView):
    model = Post
    template_name = 'home'
    context_object_name = 'all_posts_list'
