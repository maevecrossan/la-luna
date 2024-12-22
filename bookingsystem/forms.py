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
                    'placeholder': '123456789',
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
                    'min': date.today().strftime('%Y-%m-%d'),
                }
            ),
            'time': forms.Select(
                attrs={
                    'id': 'time',
                    'name': 'time',
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
        # Get user from kwargs (passed from the view)
        user = kwargs.pop('user', None)

        # Initialize the form
        super().__init__(*args, **kwargs)

        # Restrict user from clicking dates in the past
        self.fields['date'].widget.attrs[
            'min'] = date.today().strftime('%Y-%m-%d')

        # Prepopulate the email field with the logged-in user's email
        if user and user.email:
            self.fields['email'].initial = user.email

        # If your model has a CLOSED_DATES field, pass it to the form
        if hasattr(self.instance, 'CLOSED_DATES'):
            self.fields['date'].disabled_dates = self.instance.CLOSED_DATES

    def disabled_dates(self):
        """
        Prevents bookings on closed dates.
        """
        return self.fields['date'].disabled_dates

    def clean_date(self):
        """
        Validate the date field to ensure:
        - It is not empty.
        - It is not a date in the past.
        - It is not a closed date.
        """
        date_value = self.cleaned_data.get('date')
        if not date_value:
            raise forms.ValidationError(
                "The date field is required.")
        if date_value < date.today():
            raise forms.ValidationError(
                "The booking date cannot be in the past.")
        if date_value in self.instance.CLOSED_DATES:
            # `self.instance` refers to the Booking model instance
            raise forms.ValidationError(
                f"The restaurant is closed on {date_value}.\
                    Please select another date.")
        return date_value
