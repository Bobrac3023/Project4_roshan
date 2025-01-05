from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "requested"), (1, "confirmed"))

# Create your models here.
class Reservation(models.Model):
    title = models.CharField(max_length=200, unique=True)
    patron = models.ForeignKey(
    User, on_delete=models.CASCADE, related_name="patron_name"
    )
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    
class Feedback (models.Model):  
    post = models.ForeignKey(
        Reservation, on_delete=models.CASCADE, related_name="comments")
    patron = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter")
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    
    
    
