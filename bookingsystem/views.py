"""
Contains booking form logic
"""

from datetime import date
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Booking
from .forms import BookingForm


# Create your views here.


@login_required
def booking_system(request):
    """
    Handles booking form submission. 
    Saves valid data to the database.
    """

    form = BookingForm()
    today = date.today().strftime('%d-%m-%Y')

    if request.method == 'POST':
        print("Received a POST request") #debugging
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            form.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Booking successfully submitted.')
            print("Form submitted") #debugging
            return redirect('bookingsystem:my-bookings')
        else:
            messages.add_message(
                request, messages.ERROR,
                'Error submitting booking.')
            print("Form error") #debugging
    return render(request, 'bookings.html', {'form': form, 'today': today})


@login_required
def booking_list(request):
    """
    Allows booking_list.html to display bookings for authenticated users.
    """
    # Check if the user is authenticated before making a query based on request.user
    if request.user.is_authenticated:
        # Filter bookings
        bookings = Booking.objects.filter(user=request.user)

        # Return the filtered booking list template with bookings context
        return render(request, 'booking_list.html', {'bookings': bookings})

    else:
        messages.error(request, "You must be logged in to view your bookings.")
        return redirect('login')


def booking_edit(request, booking_id):
    """
    View to edit bookings.

    Populates booking form with relevant details.
    """
    booking = get_object_or_404(
        Booking, id=booking_id, user=request.user
        )

    if request.method == "POST":
        booking_form = BookingForm(request.POST, instance=booking)

        # Validate the form and check ownership again for extra safety
        if booking_form.is_valid() and booking.user == request.user:
            booking_form.save()
            messages.add_message(request, messages.SUCCESS,
                                 'Booking successfully submitted.')
            return redirect('bookingsystem:my-bookings')
        else:
            messages.add_message(request, messages.ERROR,
                                 'Error submitting booking.')
            return redirect('bookingsystem:my-bookings')
    else:
        booking_form = BookingForm(instance=booking)

    return render(request, 'bookings.html', {'form': booking_form, 'booking': booking})


def booking_delete(request, booking_id):
    """
    View to delete bookings.
    """
    booking = get_object_or_404(
        Booking, id=booking_id, user=request.user)

    if booking.user == request.user:
        booking.delete()
        messages.add_message(request, messages.SUCCESS, 'Booking deleted!')
    return redirect('bookingsystem:my-bookings')
