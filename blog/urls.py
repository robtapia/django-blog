from django.urls import path

from .views import BlogListView

urlPatterns = [
    path('', BlogListView.as_view(), name='home'),
]