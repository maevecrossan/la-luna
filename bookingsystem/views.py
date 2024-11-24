from django.shortcuts import render
from django.views import generic
from .models import Booking
from .forms import BookingForm


# Create your views here.
def booking_system(request):
    form = BookingForm()
    return render(request, '../templates/bookings.html', {'form': form})
