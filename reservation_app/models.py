from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime


STATUS = ((0, "requested"), (1, "confirmed"))


class Reservation(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(default=True)
    message = models.TextField(max_length=150)
    date = models.DateField(default=timezone.now)
    time = models.TimeField(default=timezone.now)
    guests = models.IntegerField(default=0)
    read = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    
class Meta:
    """
        Metadata options for the model.
        Attributes:
        unique_together (tuple): Ensures that the combination of 'table',
        'date', and 'time' is unique.
    """
    unique_together = ('date', 'time')

    def __str__(self):
        """
        Returns a string representation of the Reservation instance.
             The string includes the name, number of guests,
             date, and time information.
        """
        return (f'Dear {self.name}, your booking for {self.guests}'
                f'guests on {self.date} at {self.time} is'
                f'confirmed')

class Feedback (models.Model):
    post = models.ForeignKey(
        Reservation, on_delete=models.CASCADE, related_name="comments")
    patron = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter")
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
        