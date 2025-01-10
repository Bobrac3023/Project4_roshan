from .models import Reservation
from django import forms
#from .forms import ReservationForm
from django.shortcuts import render

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ('name', 'email', 'message')


#def about_me(request):
#    """
#    Renders the About page
#    """
#    Reservation = Reservation.objects.all().order_by('-updated_on').first()
#    collaborate_form = ReservationForm()

#    return render(
#        request,
#        "reservation/index.html",
#        {
#            "Reservation": Reservation,
#            "collaborate_form": collaborate_form
#        },
#    )