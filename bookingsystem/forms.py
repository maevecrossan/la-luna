from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    """
    Booking Form Template
    """
    fields = ['name', 'phone_number', 'email', 'date', 'time', 'guests']
    widgets = {
        'name': forms.TextInput(attrs={'placeholder': 'Full Name', 'class': 'formbold-form-input'}),
        'phone_number': forms.TextInput(attrs={'placeholder': 'Phone Number', 'class': 'formbold-form-input'}),
        'email': forms.EmailInput(attrs={'placeholder': 'Email Address', 'class': 'formbold-form-input'}),
        'date': forms.DateInput(attrs={'type': 'date', 'class': 'formbold-form-input'}),
        'time': forms.Select(attrs={'class': 'formbold-form-input'}),
        'guests': forms.Select(attrs={'class': 'formbold-form-input'}),
        }
    
    class Meta:
        model = Booking