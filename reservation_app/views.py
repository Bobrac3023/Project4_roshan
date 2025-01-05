from django.shortcuts import render
#from django.http import HttpResponse
from django.views import generic
from .models import Reservation


# Create your views here.
#def myreservation (request):
    #return HttpResponse ("Welcome to Roshan's reservation system")

class PostList(generic.ListView):
    model = Reservation
    queryset = Reservation.objects.all()
    template_name = "reservation_app_index.html"