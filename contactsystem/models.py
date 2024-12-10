from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

class Contact(models.Model):
    """Model for contact form submission"""

    contact_name = models.CharField(
        max_length=100,
        blank=False,
        null=False,
    )

    contact_phone_number = models.CharField(
        max_length=15,
        validators=[  # Source: geeksforgeeks.org
            RegexValidator(
                regex=r'^\+?1?\d{9,15}$',
                message="Please enter a valid phone number. Up to 15 digits allowed."
            )
        ]  # minimal validation added as this is not main method of contact
    )

    contact_email = models.EmailField(
        max_length=250,
        null=False,
        blank=False,
    )

    contact_message = models.TextField(
        max_length=500,
        null=False,
        blank=False
    )
