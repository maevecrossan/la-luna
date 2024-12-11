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
            form.save()  # Save the form to the database
            messages.add_message(
                request, messages.SUCCESS,
                'Message successfully sent.')
        else:
            messages.add_message(
                request, messages.ERROR,
                'Error sending message.')
    return render(request, 'contact.html', {'form': form})
