from datetime import date
from .models import Booking
from django import forms

class BookingForm(forms.ModelForm):
    """
    Booking Form Template
    """
    class Meta:
        model = Booking
        fields = ['name', 'phone_number', 'email', 'date', 'time', 'guests']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Full Name', 'class': 'formbold-form-input'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'Phone Number', 'class': 'formbold-form-input'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email Address', 'class': 'formbold-form-input'}),
            'date': forms.DateInput(
                attrs={
                    'type': 'date',
                    'class': 'formbold-form-input',
                }
            ),
            'time': forms.Select(attrs={'class': 'formbold-form-input'}),
            'guests': forms.Select(attrs={'class': 'formbold-form-input'}),
            }
        
    def __init__(self, *args, **kwargs):
        """
        Prevents bookings in the past.
        """
        super().__init__(*args, **kwargs)
        self.fields['date'].widget.attrs['min'] = date.today().strftime('%Y-%m-%d')