from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

# Create your models here.


class Booking(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="bookings"
    )
    phone_number = models.CharField(
        max_length=15,  
        validators=[ # Source: geeksforgeeks.org
            RegexValidator(
                regex=r'^\+?1?\d{9,15}$',
                message="Please enter a valid phone number. Up to 15 digits allowed."
            )
        ]
    )
    date = models.DateField()
    TIME_OPTIONS = [
        ("15:00", "3:00 PM"),
        ("15:30", "3:30 PM"),
        ("16:00", "4:00 PM"),
        ("16:30", "4:30 PM"),
        ("17:00", "5:00 PM"),
        ("17:30", "5:30 PM"),
        ("18:00", "6:00 PM"),
        ("18:30", "6:30 PM"),
        ("19:00", "7:00 PM"),
        ("19:30", "7:30 PM"),
        ("20:00", "8:00 PM"),
        ("20:30", "8:30 PM"),
        ("21:00", "9:00 PM"),
        ("21:30", "9:30 PM"),
        ("22:00", "10:00 PM"),
    ]
    time = models.CharField(max_length=5, choices=TIME_OPTIONS)
    GUEST_OPTIONS = [
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),
        ("6", "6"),
        ("7", "7"),
        ("8", "8"),
    ]
    guests = models.CharField(max_length=1, choices=GUEST_OPTIONS)