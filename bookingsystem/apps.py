""" App registry """

from django.apps import AppConfig


class BookingsystemConfig(AppConfig):
    """ bookingsystem app registration """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bookingsystem'
