from django.shortcuts import render,get_object_or_404, reverse
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
    #reservation_app=Reservation.objects.all()    
    about = Reservation.objects.all()
    #about = Reservation.objects.all().order_by('-updated_on').first()
    reservation_form = ReservationForm()

    return render(
        request,
        "reservation/index.html",
            {
            """
            adding reservation an reservation form variables to the context in the render helper function
            """
            "about": about,
            "reservation_form": reservation_form
            },
    )


def comment_edit(request,booking_id):
    """
    view to edit comments
    """
    if request.method == "POST":

        queryset = Reservation.objects()
        username = get_object_or_404(queryset)
        username = get_object_or_404(queryset,name=username)
        username = get_object_or_404(Reservation, pk=username_id)
        """
        ensure reservation_form variable is connected to the correct database record instance to be edited?
        """
        reservation_form = ReservationForm(data=request.Reservation, instance=username)

        if reservation_form.is_valid() and name.username == request.user:
            username = reservation_form.save(commit=False)
            username.username = username
            username.approved = False
            username.save()
            messages.add_message(request, messages.SUCCESS, 'Reservation Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('index.html', args=[messages]))

