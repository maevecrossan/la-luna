"""
Contains booking form logic
"""

from datetime import date
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import generic
from django.contrib import messages
from .models import Booking
from .forms import BookingForm


# Create your views here.

class BookingList(generic.ListView):
    """
    Allows booking_list.html to display bookings for users.
    """
    model = Booking
    template_name = "booking_list.html"
    context_object_name = 'bookings'

    def get_queryset(self):
        """Override to order bookings by date and time."""
        return Booking.objects.all().order_by('-date', '-time')


def booking_system(request):
    """
    Handles booking form submission. 
    Saves valid data to the database.
    """

    form = BookingForm()
    today = date.today().strftime('%Y-%m-%d')

    if request.method == 'POST':
        form = BookingForm(request.POST)
        print("POST data received")  # debugging
        if form.is_valid():
            form.save()
            messages.add_message(
        request, messages.SUCCESS,
        'Booking successfully created.')
            return HttpResponseRedirect('/')
        else:
            print("ERROR:", form.errors)  # debugging
    return render(request, '../templates/bookings.html', {'form': BookingForm(), 'today': today})
