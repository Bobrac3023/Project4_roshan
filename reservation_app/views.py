
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.views import generic
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .models import Reservation, Feedback
from .forms import ReservationForm, FeedbackForm
"""
Validating reservations using model rules.
Preventing past-date bookings and over-guest limits.
Securely protecting update/delete actions with login requirements.
"""
# ----------------------------
# Homepage View (ListView style)
# ----------------------------


class PostList(generic.ListView):
    model = Reservation
    queryset = Reservation.objects.all()
    template_name = "reservation/index.html"  # uses reservation/index.html


# ----------------------------
# About Page View (Handles Feedback)
# ----------------------------

def about_me(request):
    if request.method == "POST" and "feedback_submit" in request.POST:
        feedback_form = FeedbackForm(request.POST)
        if feedback_form.is_valid():
            feedback = feedback_form.save(commit=False)
            if request.user.is_authenticated:
                feedback.patron = request.user
            feedback.save()
            messages.success(request, "Thank you for your feedback!")
            return redirect('about')
    else:
        feedback_form = FeedbackForm()

    feedbacks = Feedback.objects.order_by('-created_on')[:5]

    return render(
        request,
        "reservation/about.html",  # Make sure your template is named correctly
        {
            "feedback_form": feedback_form,
            "feedbacks": feedbacks
        }
    )
# ----------------------------
# Reservation Form Page (at /reservation/form/)
# ----------------------------


def reservation_form(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():  # validates form field rules
            reservation = form.save(commit=False)
            reservation.full_clean()  # Enforce model-level validation
            if request.user.is_authenticated:
                reservation.user = request.user
            reservation.save()
            messages.success(request, "Reservation submitted successfully!")
            return redirect('reservation_list')
    else:
        form = ReservationForm()
    return render(request, 'reservation/reservation_form.html', {'form': form})


"""
Only logged-in users can use this (protected by @login_required)
Shows the reservation in a form so the user can edit it
Saves and shows a message when updated or deleted
"""
# ----------------------------
# Update Reservation
# ----------------------------


@login_required
def update_reservation(request, pk):
    try:
        reservation = Reservation.objects.get(pk=pk, user=request.user)
    except Reservation.DoesNotExist:
        # Friendly message if reservation not found or not owned by user
        messages.error(request, "Reservation not found")
        return redirect('reservation_list')
    if request.method == 'POST':
        form = ReservationForm(request.POST, instance=reservation)

        if form.is_valid():  # validates form field rules
            reservation = form.save(commit=False)
            reservation.full_clean()  # Enforce model-level validation
            reservation.save()
            messages.success(request, 'Reservation updated successfully')
            return redirect('reservation_list')
    else:
        form = ReservationForm(instance=reservation)
    return render(request, 'reservation/update_reservation.html',
                  {'form': form})


"""
Only logged-in users can delete (protected by @login_required)
Shows a confirmation page first
If user clicks “Yes” → Deletes reservation
"""
# ----------------------------
# Delete Reservation
# ----------------------------


@login_required
def delete_reservation(request, pk):
    try:
        reservation = Reservation.objects.get(pk=pk, user=request.user)
    except Reservation.DoesNotExist:
        # Friendly message if reservation not found or not owned by user
        messages.error(request, "Reservation not found")
        return redirect('reservation_list')

    if request.method == 'POST':
        reservation.delete()
        messages.success(request, 'Reservation cancelled successfully!')
        return redirect('reservation_list')
    return render(request, 'reservation/confirm_delete.html',
                  {'reservation': reservation})
# ----------------------------
# List of Reservations by Logged-In User
# ----------------------------


@login_required
def reservation_list(request):
    reservations = Reservation.objects.filter(user=request.user)
    return render(request, 'reservation/reservation_list.html',
                  {'reservations': reservations})


def contact_us(request):
    return render(request, 'reservation/contact.html')
