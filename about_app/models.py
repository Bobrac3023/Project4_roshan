from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Review (models.Model):
    fullname = models.ForeignKey(
    User, on_delete=models.CASCADE, related_name="name"
    )
    feedback = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    

    
    
    
