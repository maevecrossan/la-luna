"""This file houses the contact form django template."""

from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """
    Contact form template
    """
    class Meta:
        """
        Contact form fields
        """
        model = Contact
        fields = ['contact_name', 'contact_phone_number',
                  'contact_email', 'contact_message']
        widgets = {
            'contact_name': forms.TextInput(
                attrs={
                    'id': 'contact_name',
                    'name': 'contact_name',
                    'placeholder': 'Full Name',
                    'class': 'formbold-form-input'
                }
            ),
            'contact_phone_number': forms.TextInput(
                attrs={
                    'id': 'contact_phone_number',
                    'name': 'contact_phone_number',
                    'placeholder': '123456789',
                    'class': 'formbold-form-input',
                    'pattern': r'^\+?1?\d{9,15}$',
                }
            ),
            'contact_email': forms.EmailInput(
                attrs={
                    'id': 'contact_email',
                    'name': 'contact_email',
                    'placeholder': 'Email Address',
                    'class': 'formbold-form-input'
                }
            ),
            'contact_message': forms.Textarea(
                attrs={
                    'id': 'contact_message',
                    'name': 'contact_message',
                    'placeholder': 'Your Message',
                    'class': 'formbold-form-input',
                    'rows': 4,
                }
            )
        }
