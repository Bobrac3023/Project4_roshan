from django.shortcuts import render
from django.views import generic
from .models import Review

# Create your views here.

class PostList(generic.ListView):
    model = Review
    queryset = Review.objects.all()
    template_name="about/about.html"
    #paginate_by = 6