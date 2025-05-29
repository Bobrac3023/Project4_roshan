from django.shortcuts import render, redirect
from reservation_app.forms import ReservationForm, FeedbackForm
from django.contrib import messages
from reservation_app.forms import FeedbackForm
from reservation_app.models import Feedback #using Feedback from reservation_app




def about_me(request):
    reservation_form = ReservationForm()
    feedback_form = FeedbackForm()

    if request.method == "POST":
        if 'reservation_submit' in request.POST:
            reservation_form = ReservationForm(request.POST)
            if reservation_form.is_valid():
                reservation = reservation_form.save(commit=False)
                if request.user.is_authenticated:
                    reservation.user = request.user
                reservation.save()
                messages.success(request, "Reservation request received.")
                return redirect('about')

        elif 'feedback_submit' in request.POST:
            feedback_form = FeedbackForm(request.POST)
            if feedback_form.is_valid():
                feedback = feedback_form.save(commit=False)
                if request.user.is_authenticated:
                    feedback.patron = request.user
                feedback.save()
                messages.success(request, "Thank you for your feedback!")
                return redirect('about')

    feedbacks = Feedback.objects.order_by('-created_on')[:5]
    return render(request, "reservation/about.html", {
        "reservation_form": reservation_form,
        "feedback_form": feedback_form,
        "feedbacks": feedbacks,
    })
