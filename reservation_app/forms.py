from .models import Reservation
from django import forms
from django.shortcuts import render

class ReservationForm(forms.ModelForm):
    """
    Form for creating and updating reservations.
    Fields:
    name (CharField): The name of the guest making the reservation.
    email (EmailField) : Eail of the guest for the reservation 
    message (TextField) : Additonal notes from the guest
    date (DateField): Only from current date is accepted.
    time (CharField): Can choose only from the given time slots.
    guests (IntegerField): The number of guests.
        
    """

    name = forms.CharField(max_length=100, 
                           widget=forms.TextInput(
                               attrs={'class': 'form-control'}))
    guests = forms.IntegerField(widget=forms.NumberInput(
                                    attrs={'class': 'form-control'}))
    
    message = forms.CharField(
        max_length=150,
        widget=forms.Textarea(
            attrs={'class': 'form-control', 'maxlength': 150}
        )
    )


    class Meta:
        model = Reservation
        fields = ('name', 'email', 'message','date','time','guests')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'time': forms.Select(choices=[
                ('12:00', '12:00 PM'), ('12:15', '12:15 PM'),
                ('12:30', '12:30 PM'), ('12:45', '12:45 PM'),
                ('13:00', '1:00 PM'), ('13:15', '1:15 PM'),
                ('13:30', '1:30 PM'), ('13:45', '1:45 PM'),
                ('14:00', '2:00 PM'), ('14:15', '2:15 PM'),
                ('14:30', '2:30 PM'), ('17:30', '5:30 PM'),
                ('17:45', '5:45 PM'), ('18:00', '6:00 PM'),
                ('18:15', '6:15 PM'), ('18:30', '6:30 PM'),
                ('18:45', '6:45 PM'), ('19:00', '7:00 PM'),
                ('19:15', '7:15 PM'), ('19:30', '7:30 PM'),
                ('19:45', '7:45 PM'), ('20:00', '8:00 PM'),
                ('20:15', '8:15 PM'), ('20:30', '8:30 PM'),
                ('20:45', '8:45 PM'), ('21:00', '9:00 PM'),
                ('21:15', '9:15 PM'), ('21:30', '9:30 PM'),
                ('21:45', '9:45 PM'), ('22:00', '10:00 PM')
            ], attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            }),
            'message': forms.Textarea(attrs={'class': 'form-control'}),
        }

  

   