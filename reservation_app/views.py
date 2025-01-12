from django.shortcuts import render,get_object_or_404,reverse
from django.http import HttpResponseRedirect
from django.views import generic
from django.contrib import messages
from .models import Reservation
from .forms import ReservationForm
from django.utils.decorators import method_decorator
# Create your views here.

class PostList(generic.ListView):
    model = Reservation
    queryset = Reservation.objects.all()
    template_name="reservation/index.html"
    


def about_me(request):
    """
        Renders the index.html page
        """
    if request.method == "POST":
        reservation_form = ReservationForm(data=request.POST)
        if reservation_form.is_valid():
            reservation_form.save()
            messages.add_message(request, messages.SUCCESS, "Reservation request received. Please check your inbox for an confirmation email")
        
    about = Reservation.objects.all()
    reservation_form = ReservationForm()
    return render(
        request,
        "reservation/index.html",
            {
            """
            adding reservation an reservation form variables to the context in the render helper function
            """
            "about": about,
            "reservation_form": reservation_form}
    )

           