""" Sets paramaters for the booking app for administrative viewing. """

from django.contrib import admin
from .models import Booking
from .forms import BookingForm


class BookingAdmin(admin.ModelAdmin):
    """
    Set parameters and layout for booking app on the admin page.
    """
    form = BookingForm
    list_display = (
        'name', 'date', 'time', 'guests',
        'email', 'phone_number', 'expired_status'
        )
    list_filter = (
        'date', 'time'
        )
    search_fields = (
        'name', 'email'
        )
    actions = [
        'delete_selected'
        ]

    @admin.display(boolean=True, description='Expired')
    def expired_status(self, obj):
        """
        Displays expired field for admin
        """
        return obj.expired


# Register your models here.
admin.site.register(Booking, BookingAdmin)
