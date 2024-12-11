"""
Register app-level models.
"""

from django.contrib import admin
from .models import Contact
from .forms import ContactForm


class ContactAdmin(admin.ModelAdmin):
    """
    Set parameters for admin page.
    """
    form = ContactForm
    list_display = ('contact_name', 'contact_phone_number',
                    'contact_email', 'contact_message')


# Register your models here.


admin.site.register(Contact, ContactAdmin)
