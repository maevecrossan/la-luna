from django.contrib import admin
from .models import Booking
from .forms import BookingForm

class BookingAdmin(admin.ModelAdmin):
    form = BookingForm
    list_display = ('name', 'date', 'time', 'guests', 'email', 'phone_number')
    list_filter = ('date', 'time')  # Add filters for better organization
    search_fields = ('name', 'email')  # Allow searching by these fields


# Register your models here.
admin.site.register(Booking, BookingAdmin)