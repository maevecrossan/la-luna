""" App registry """

from django.apps import AppConfig


class ContactsystemConfig(AppConfig):
    """ contactsystem app registration """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'contactsystem'
