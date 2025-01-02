from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def myreservation (request):
    return HttpResponse ("Welcome to Roshan's reservation system")

