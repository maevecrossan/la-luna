from django.shortcuts import render
from django.views import generic
from .models import Booking
from .forms import BookingForm
from datetime import date


# Create your views here.
def booking_system(request):
    form = BookingForm()
    today = date.today().strftime('%Y-%m-%d')
    return render(request, '../templates/bookings.html', {'form': form, 'today': today})
