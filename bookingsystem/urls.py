"""
URLs for list of bookings and editing bookings.
"""

from django.urls import path
from . import views

urlpatterns = [
    path('edit-booking/<int:booking_id>/', views.booking_edit, name='booking-edit'),
    path('my-bookings/', views.booking_list, name='my-bookings'),
]
