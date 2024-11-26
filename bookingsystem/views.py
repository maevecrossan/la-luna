from django.shortcuts import render
from django.views import generic
from .models import Booking
from .forms import BookingForm
from datetime import date, timedelta


# Create your views here.
def booking_system(request):
    form = BookingForm()
    today = date.today().strftime('%Y-%m-%d')
    
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save() 
            # return redirect('../templates/bookings.html') edit to redirect to user bookings
    return render(request, '../templates/bookings.html', {'form': form, 'today': today})
