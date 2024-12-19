""" This file houses the contact model """

from django.db import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

# Create your models here.


# Custom validator for phone number minimum length
def validate_min_length(value):
    """Ensure the number has at least 10 digits"""

    if len(value.replace("+", "").replace(" ", "")) < 9:
        raise ValidationError(
            "Phone number must have between 9 and 15 digits."
        )


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
                message="Please enter a valid phone number. \
                Between 9 and 15 digits allowed."
            ),
            validate_min_length,
        ]
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

    is_resolved = models.BooleanField(
        default=False,
        help_text="Mark this as resolved when the query is handled.",
    )


def __str__(self):
    return self.contact_name
