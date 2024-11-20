from django.shortcuts import render
from django.views import generic
from .models import Booking


# Create your views here.
def booking_system(request):
    return render(request, '../templates/bookings.html')
