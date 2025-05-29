from django import forms
from .models import Reservation, Feedback
import datetime

class ReservationForm(forms.ModelForm):
    # ✅ Custom time slot choices (adjust to your needs)
    TIME_CHOICES = [
        ("12:00", "12:00 PM"),
        ("12:30", "12:30 PM"),
        ("13:00", "1:00 PM"),
        ("13:30", "1:30 PM"),
        ("14:00", "2:00 PM"),
        ("19:00", "7:00 PM"),
        ("19:30", "7:30 PM"),
        ("20:00", "8:00 PM"),
    ]

    # ✅ Override time field to use dropdown
    time = forms.ChoiceField(
        choices=TIME_CHOICES,
        widget=forms.Select(attrs={
            'class': 'form-control',
        })
    )

    # ✅ Override date field to use calendar and restrict past dates
    date = forms.DateField(
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': 'form-control',
            'min': datetime.date.today().strftime('%Y-%m-%d'),  # disables past dates
        })
    )

    class Meta:
        model = Reservation
        fields = ['name', 'email', 'message', 'date', 'time', 'guests']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '👤 Your Name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': '✉️ Your Email'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': '💬 Add a message or request...',
                'rows': 3
            }),
            'guests': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '👥 Number of Guests'
            }),
        }


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': '📝 Share your feedback...',
                'rows': 4
            })
        }
