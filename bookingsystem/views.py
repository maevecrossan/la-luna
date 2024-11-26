from django.shortcuts import render, redirect
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from .models import Booking
from .forms import BookingForm
from datetime import date, timedelta
import logging


# Create your views here.

def booking_system(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            print(f"Form errors: {form.errors}")  # Log validation errors
    return render(request, '../templates/bookings.html', {'form': BookingForm()})