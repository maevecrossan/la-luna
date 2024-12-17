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
                    'contact_email',  'is_resolved')
    list_filter = ("is_resolved",)
    search_fields = ("contact_name", "contact_email")


# Register your models here.

admin.site.register(Contact, ContactAdmin)
