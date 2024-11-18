from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def booking_system(request):
    return HttpResponse("Hello, Booking System!")