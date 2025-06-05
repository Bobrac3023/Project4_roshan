from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime


STATUS = (
    (0, "Requested"),
    (1, "Confirmed"),
)


class Reservation(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True
    )
    name = models.CharField(max_length=100)
    email = models.EmailField(default=True)
    message = models.TextField(max_length=75)
    date = models.DateField(default=timezone.now)
    time = models.TimeField(default=timezone.now)
    guests = models.IntegerField(default=0)
    read = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    def clean(self):
        # Combine date and time into one datetime
        reservation_datetime = datetime.datetime.combine(
            self.date, self.time
        )

        # Make reservation_datetime timezone-aware
        reservation_datetime = timezone.make_aware(
            reservation_datetime,
            timezone.get_current_timezone()
        )

        # Prevent past reservations
        if reservation_datetime < timezone.now():
            raise ValidationError(
                "Reservation date/time cannot be in the past"
            )

        # Guest count must be between 1 and 10
        if self.guests < 1:
            raise ValidationError("Number of guests must be at least 1.")

        if self.guests > 10:
            raise ValidationError("Reservations cannot exceed 10 guests.")

    def __str__(self):
        return f"Reservation request form {self.name}"


class Feedback(models.Model):
    reservation = models.ForeignKey(
        'Reservation',
        on_delete=models.CASCADE,
        related_name="feedbacks",
        null=True,
        blank=True
    )
    patron = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="feedbacks",
        null=True,
        blank=True
    )
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        username = self.patron.username if self.patron else "Anonymous"
        return f"Feedback by {username}"
