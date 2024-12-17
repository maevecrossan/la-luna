"""
This file houses the booking model.

Also dealt with below is the CRUD functionality.

"""

from datetime import datetime, timedelta, date as dt_date
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.utils import timezone


# Custom validator for phone number minimum length
def validate_min_length(value):
    """Ensure the number has at least 10 digits"""

    if len(value.replace("+", "").replace(" ", "")) < 9:
        raise ValidationError(
            "Phone number must have between 9 and 15 digits."
        )


# Create your models here.


class Booking(models.Model):
    """Model for booking a table."""

    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name="bookings",
    )

    name = models.CharField(
        max_length=100,
        blank=False,
        null=False,
    )

    email = models.EmailField(
        max_length=250,
        null=False,
        blank=False,
    )

    phone_number = models.CharField(
        max_length=15,
        validators=[  # Source: geeksforgeeks.org
            RegexValidator(
                regex=r'^\+?1?\d{9,15}$',
                message="Please enter a valid phone number."
            ),
            validate_min_length,
        ]
    )

    date = models.DateField(
        null=False,
        blank=False
    )

    CLOSED_DATES = [
        dt_date(2024, 12, 25),
        dt_date(2025, 12, 25),
        dt_date(2026, 12, 25),
        dt_date(2027, 12, 25),
        dt_date(2025, 1, 1),
        dt_date(2026, 1, 1),
        dt_date(2027, 1, 1),
        dt_date(2028, 1, 1),
    ]

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
    guests = models.CharField(
        max_length=1,
        choices=GUEST_OPTIONS,
        null=False,
        blank=False)

    end_time = models.TimeField(null=True, blank=True)

    objects = models.Manager()

    def is_restaurant_closed(self):
        """
        Check if the given date is a restaurant closure date.
        """
        return self.date in self.CLOSED_DATES

    def save(self, *args, **kwargs):
        """
        Calculates the end time (adds two hours to
        'time') and stores it to the database.

        Database use only (not visible to admin or user).
        """

        if self.time:

            # Convert the 'time' string to datetime.time object
            start_time_obj = datetime.strptime(self.time, '%H:%M').time()

            # Combine the 'date' and 'start_time_obj' into datetime object
            start_datetime = datetime.combine(self.date, start_time_obj)

            # Add two hours to the start time to calculate the end time
            end_datetime = start_datetime + timedelta(hours=2)

            # Store the calculated end time
            self.end_time = end_datetime.time()

        super().save(*args, **kwargs)

    def clean(self):
        """
        Custom validation to prevent overlap in bookings
        and tally capacity (max 40 ppl).
        """

        if not self.date:
            raise ValidationError("The date field is required.")

        # Access the date from the form data
        selected_date = self.date

        if selected_date in self.CLOSED_DATES:
            raise ValidationError(f"The restaurant is closed on {
                                selected_date}. Please select another date.")

        if self.time:
            start_datetime = (
                datetime.combine(
                    self.date, datetime.strptime(self.time, '%H:%M').time()
                )
            )
            end_datetime = start_datetime + timedelta(hours=2)

            # Convert 'end_datetime' to time to use in comparisons
            end_time = end_datetime.time()

            overlapping_bookings = Booking.objects.filter(
                date=self.date,
                # Existing booking ends after new start time
                end_time__gt=start_datetime.time(),
                # Existing booking starts before new end time
                time__lt=end_time,
            )

            # Calculate total number of guests during overlapping time slots
            total_guests = sum(
                int(booking.guests) for booking in overlapping_bookings)

            # Check if adding this booking would exceed capacity
            if total_guests + int(self.guests) > 40:
                raise ValidationError(
                    "We cannot accommodate your group size at this time."
                    "Please reduce your guest count or try another time slot.")

            if self.is_restaurant_closed():  # No conflict with dt_date
                raise ValidationError(
                    f"The restaurant is closed on {self.date}.\
                        Please select another date.")

    @property
    def expired(self):
        """
        If reservation time and date has passed current time and date,
        booking will be marked 'expired'.

        Otherwise will be labelled as 'active'.
        """
        if self.date and self.time:
            # Combine the booking date and start time to get the full datetime

            # Convert start time string to time object
            start_time_obj = datetime.strptime(self.time, '%H:%M').time()

            # Combine date and time to create a datetime object
            start_datetime = datetime.combine(self.date, start_time_obj)

            # Make sure the datetime is timezone-aware
            local_timezone = timezone.get_current_timezone()
            start_datetime = timezone.make_aware(
                start_datetime,
                timezone=local_timezone
            )

            # Compare current time with the booking's start time
            return timezone.now() > start_datetime
        return False
