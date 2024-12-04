from django.urls import path
from . import views

urlpatterns = [
    path('my-bookings/', views.BookingList.as_view(), name='my-bookings'),
    path('edit-booking/<int:booking_id>/', views.booking_edit, name='booking-edit'),
]
