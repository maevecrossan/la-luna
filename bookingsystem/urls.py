"""
URLs for list of bookings and editing bookings.
"""

from django.urls import path
from . import views

app_name = 'bookingsystem'

urlpatterns = [
    path(
        "",
        views.booking_system,
        name="bookings"
     ),

    path('delete-booking/<int:booking_id>/',
         views.booking_delete,
         name='booking-delete'),

    path('edit-booking/<int:booking_id>/',
         views.booking_edit,
         name='booking-edit'),

    path('my-bookings/',
         views.booking_list,
         name='my-bookings'),
]
