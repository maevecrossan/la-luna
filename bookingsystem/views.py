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

    form = BookingForm(user=request.user)
    today = date.today().strftime('%d-%m-%Y')

    if request.method == 'POST':
        form = BookingForm(request.POST, user=request.user)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            form.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Booking successfully submitted.')
            return redirect('bookingsystem:my-bookings')
        else:
            messages.add_message(
                request, messages.ERROR,
                'Error submitting booking.')
    return render(request, 'bookings.html', {'form': form, 'today': today})


@login_required
def booking_list(request):
    """
    Allows booking_list.html to display bookings for the relevant
    authenticated user, organized by month with nearest reservations
    at the top and expired ones at the bottom.
    """
    # Check if the user is authenticated before making a query
    # based on request.user
    if request.user.is_authenticated:
        # Get the user's bookings
        bookings = Booking.objects.filter(
            user=request.user).order_by('date', 'time')

        # Separate bookings into upcoming and
        # expired using the `expired` property
        upcoming_bookings = [
            booking for booking in bookings if not booking.expired]
        expired_bookings = [
            booking for booking in bookings if booking.expired]

        # Pass the bookings and current date to the template
        return render(request, 'booking_list.html', {
            'upcoming_bookings': upcoming_bookings,
            'expired_bookings': expired_bookings,
            'today': date.today(),  # Current date to use in the template
        })
    else:
        messages.error(request, "You must be logged in to view your bookings.")
        return redirect('login')


def booking_edit(request, booking_id):
    """
    View to edit bookings.

    Populates booking form with relevant details.
    """

    # Retrieve the booking instance
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)

    if request.method == "POST":
        # Populate the form with POST data and the existing booking instance
        booking_form = BookingForm(data=request.POST, instance=booking)

        # Validate the form and check ownership again for extra safety
        if booking_form.is_valid():
            booking_form.save()
            messages.add_message(request, messages.SUCCESS,
                                 'Booking successfully updated.')
            return redirect('bookingsystem:my-bookings')
        else:
            messages.add_message(request, messages.ERROR,
                                 'Error updating booking.')
    else:
        # Instantiate the form with the existing booking instance
        booking_form = BookingForm(instance=booking)

    # Render the form template with additional `is_edit` context
    return render(request, 'bookings.html', {
        'form': booking_form,
        'booking': booking,
        'is_edit': True  # Set to True when editing
    })


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
