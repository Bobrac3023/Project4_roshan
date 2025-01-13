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


def __str__(self):
    return f"Reservation request form {self.name}"


class Feedback (models.Model):
    post = models.ForeignKey(
        Reservation, on_delete=models.CASCADE, related_name="comments")
    patron = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter")
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
