"""
Contains booking form logic
"""

from datetime import date
from django.shortcuts import render, get_object_or_404, reverse
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
        """
        Override to order bookings by date and time.
        """
        return Booking.objects.filter(user=self.request.user).order_by('-date', '-time')


def booking_system(request):
    """
    Handles booking form submission. 
    Saves valid data to the database.
    """

    form = BookingForm()
    today = date.today().strftime('%Y-%m-%d')

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(
        request, messages.SUCCESS,
        'Booking successfully created.')
            return HttpResponseRedirect('my-bookings')
        else:
            print("ERROR:", form.errors)  # debugging
    return render(request, 'my-bookings', {'form': form, 'today': today})


def booking_edit(request, booking_id):
    """
    View to edit bookings.
    
    Populates booking form with relevant details.
    """
    booking = get_object_or_404(Booking, id=booking_id, user=request.user, expired=False)

    if request.method == "POST":
        booking_form = BookingForm(request.POST, instance=booking)

        # Validate the form and check ownership again for extra safety
        if booking_form.is_valid() and booking.user == request.user:
            booking.save()
            messages.add_message(request, messages.SUCCESS, 'Booking Updated!')
            return HttpResponseRedirect(reverse('my-bookings'))
        else:
            messages.add_message(request, messages.ERROR, 'Error updating booking!')
            return HttpResponseRedirect(reverse('my-bookings'))

    else:
        booking_form = BookingForm(instance=booking)
        return HttpResponseRedirect(reverse('bookings'))

    return render(request, 'bookings.html', {'form': booking_form, 'booking': booking})
