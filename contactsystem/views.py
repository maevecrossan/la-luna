""" This file houses the view for the contact form """

from django.shortcuts import render
from django.contrib import messages
from .forms import ContactForm

# Create your views here.


def contact_system(request):
    """
    Handles booking form submission.
    Saves valid data to the database.
    """

    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Thank you for contacting us! Your message has been sent.')
            form = ContactForm()
        else:
            messages.add_message(
                request, messages.ERROR,
                'There was an error with your submission.\
                    Please correct the errors below.')
    return render(request, 'contact.html', {'form': form})
