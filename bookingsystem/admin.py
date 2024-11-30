from django.contrib import admin
from .models import Booking
from .forms import BookingForm

class BookingAdmin(admin.ModelAdmin):
    """
    Set parameters and layout for admin page.
    """
    form = BookingForm
    list_display = ('name', 'date', 'time', 'guests', 'email', 'phone_number', 'expired_status')
    list_filter = ('date', 'time')  # Add filters for better organization
    search_fields = ('name', 'email')  # Allow searching by these fields

    @admin.display(boolean=True, description='Expired')
    def expired_status(self, obj):
        """
        Displays expired field for admin
        """
        return obj.expired


# Register your models here.
admin.site.register(Booking, BookingAdmin)
