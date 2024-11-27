"""
Contains booking form logic
"""

from datetime import date
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import BookingForm


# Create your views here.
def booking_system(request):
    """
    Handles booking form submission. 
    Saves valid data to the database.
    """

    form = BookingForm()
    today = date.today().strftime('%Y-%m-%d')

    if request.method == 'POST':
        form = BookingForm(request.POST)
        print("POST data received") #debugging
        if form.is_valid():
            form.save()
            print("successful database submission")
            return HttpResponseRedirect('/')
        else:
            print("ERROR:", form.errors) #debugging
    return render(request, '../templates/bookings.html', {'form': BookingForm(), 'today': today})
