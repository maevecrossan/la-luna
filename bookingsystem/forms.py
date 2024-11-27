"""This file houses the form django template."""

from datetime import date
from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    """
    Booking Form Template
    """
    class Meta:
        """
        booking form fields
        """
        model = Booking
        fields = ['name', 'phone_number', 'email', 'date', 'time', 'guests']
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'id': 'name', 
                       'placeholder': 'Full Name', 
                       'class': 'formbold-form-input'
                    }
                ),
            'phone_number': forms.TextInput(
                attrs={
                    'id': 'phone', 
                    'placeholder': 'Phone Number', 
                    'class': 'formbold-form-input'
                    }
                ),
            'email': forms.EmailInput(
                attrs={
                    'id': 'email', 
                    'placeholder': 'Email Address', 
                    'class': 'formbold-form-input'
                    }
                ),
            'date': forms.DateInput(
                attrs={
                    'id': 'date', 
                    'type': 'date',
                    'class': 'formbold-form-input',
                }
            ),
            'time': forms.Select(
                attrs={
                    'id': 'time', 
                    'class': 'formbold-form-input'
                    }
                ),
            'guests': forms.Select(
                attrs={
                    'id': 'guests', 
                    'class': 'formbold-form-input'
                    }
                ),
            }

    def __init__(self, *args, **kwargs):
        """
        Prevents bookings in the past.
        """
        super().__init__(*args, **kwargs)
        self.fields['date'].widget.attrs['min'] = date.today().strftime('%Y-%m-%d')
