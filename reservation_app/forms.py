from django import forms
from .models import Reservation, Feedback

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['name', 'email', 'message', 'date', 'time', 'guests']

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Share your feedback...',
                'rows': 4
            })
        }
