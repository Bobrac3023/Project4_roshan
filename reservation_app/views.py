from django.shortcuts import render
from django.views import generic
from .models import Reservation


# Create your views here.

class PostList(generic.ListView):
    model = Reservation
    queryset = Reservation.objects.all()
    template_name="reservation/index.html"
    paginate_by = 6