from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.views import generic
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .models import Reservation
from .forms import ReservationForm


# ----------------------------
# Homepage View (ListView style)
# ----------------------------
class PostList(generic.ListView):
    model = Reservation
    queryset = Reservation.objects.all()
    template_name = "reservation/index.html"


# ----------------------------
# About Page View (Handles Form Display)
# ----------------------------
def about_me(request):
    if request.method == "POST":
        reservation_form = ReservationForm(request.POST)
        if reservation_form.is_valid():
            reservation = reservation_form.save(commit=False)
            if request.user.is_authenticated:
                reservation.user = request.user
            reservation.save()
            messages.success(request, "Reservation request received. Please check your inbox for a confirmation email.")
            return redirect('about')
    else:
        reservation_form = ReservationForm()

    about = Reservation.objects.all()

    return render(
        request,
        "reservation/index.html",
        {
            "about": about,
            "reservation_form": reservation_form
        }
    )


# ----------------------------
# Reservation Form Page (at /reservation/form/)
# ----------------------------
def reservation_form(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            if request.user.is_authenticated:
                reservation.user = request.user
            reservation.save()
            messages.success(request, "Reservation submitted successfully!")
            return redirect('reservation_list')
    else:
        form = ReservationForm()

    return render(request, 'reservation/reservation_form.html', {'form': form})


# ----------------------------
# Update Reservation
# ----------------------------
@login_required
def update_reservation(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)
    if request.method == 'POST':
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your reservation has been successfully updated!')
            return redirect('reservation_list')
    else:
        form = ReservationForm(instance=reservation)

    return render(request, 'reservation/update_reservation.html', {'form': form})


# ----------------------------
# Delete Reservation
# ----------------------------
@login_required
def delete_reservation(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)
    if request.method == 'POST':
        reservation.delete()
        messages.success(request, 'Your reservation has been successfully cancelled!')
        return redirect('reservation_list')

    return render(request, 'reservation/confirm_delete.html', {'reservation': reservation})


# ----------------------------
# List of Reservations by Logged-In User
# ----------------------------
@login_required
def reservation_list(request):
    reservations = Reservation.objects.filter(user=request.user)
    return render(request, 'reservation/reservation_list.html', {'reservations': reservations})
