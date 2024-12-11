""" This file houses the urls used by the contactsystem app """

from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact_system, name='contact'),
]
