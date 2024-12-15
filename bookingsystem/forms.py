"""This file houses the booking form django template."""

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
                    'name': 'name',
                    'placeholder': 'Full Name',
                    'class': 'formbold-form-input'
                }
            ),
            'phone_number': forms.TextInput(
                attrs={
                    'id': 'phone',
                    'name': 'phone',
                    'placeholder': 'Phone Number',
                    'class': 'formbold-form-input'
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'id': 'email',
                    'name': 'email',
                    'placeholder': 'Email Address',
                    'class': 'formbold-form-input'
                }
            ),
            'date': forms.DateInput(
                attrs={
                    'id': 'date',
                    'name': 'date',
                    'type': 'date',
                    'class': 'formbold-form-input',
                }
            ),
            'time': forms.Select(
                attrs={
                    'id': 'time',
                    'name': 'time',
                    'type': 'time',
                    'class': 'formbold-form-input'
                }
            ),
            'guests': forms.Select(
                attrs={
                    'id': 'guests',
                    'name': 'guests',
                    'class': 'formbold-form-input'
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        """
        Restricts user from clicking dates in the past.
        """
        super().__init__(*args, **kwargs)
        self.fields['date'].widget.attrs['min'] = date.today().strftime(
            '%Y-%m-%d')

    def clean_date(self):
        """
        Validate the date field to ensure:
        - It is not empty.
        - It is not a date in the past.
        """
        date_value = self.cleaned_data.get('date')
        if not date_value:
            raise forms.ValidationError("The date field is required.")
        if date_value < date.today():
            raise forms.ValidationError(
                "The booking date cannot be in the past."
            )
        return date_value
