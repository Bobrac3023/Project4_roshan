from django.shortcuts import render,get_object_or_404,reverse
from django.http import HttpResponseRedirect
from django.views import generic
from django.contrib import messages
from .models import Reservation
from .forms import ReservationForm
from django.utils.decorators import method_decorator
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
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

def update_reservation(request, pk):
    """
    View to update an existing reservation.

    Args:
        request: The HTTP request object.
        pk: The primary key of the reservation to update.

    Returns:
        HttpResponse: The rendered template displaying the reservation form.
    """
    reservation = get_object_or_404(Reservation, pk=pk, user=request.user)
    if request.method == 'POST':
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            messages.success(request,
                             'Your reservation has been successfully updated!')
            return redirect('reservation_list')
    else:
        form = ReservationForm(instance=reservation)
    return render(request, 'reservation/index.htm',
                  {'form': form}) 

@login_required
def delete_reservation(request, pk):
    """
    View to delete a reservation.

    Args:
        request: The HTTP request object.
        pk: The primary key of the reservation to delete.

    Returns:
        HttpResponse: The rendered template confirming the deletion
        of the reservation.
    """
    reservation = get_object_or_404(Reservation, pk=pk, user=request.user)
    if request.method == 'POST':
        reservation.delete()
        messages.success(request,
                         'Your reservation has been successfully cancelled!')
        return redirect('reservation_list')
    return render(request, 'reservation/confirm_delete.html',
                  {'reservation': reservation})