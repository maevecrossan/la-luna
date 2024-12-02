from django.urls import path
from . import views

urlpatterns = [
    path('my-bookings/', views.BookingList.as_view(), name='my-bookings'),
]
