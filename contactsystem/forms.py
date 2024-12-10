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
                    'placeholder': 'Phone Number',
                    'class': 'formbold-form-input'
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
                    'placeholder': 'Your Message',
                    'class': 'formbold-form-input',
                    'rows': 4,
                }
            )
        }
