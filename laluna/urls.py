"""
URL configuration for laluna project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from bookingsystem.views import booking_system
from laluna.views import index, menu, contact

urlpatterns = [
    path("accounts/", include("allauth.urls")),
    path('admin/', admin.site.urls),
    path('bookings/', booking_system, name='bookings'),
    path('', include('bookingsystem.urls')),
    path('contact/', contact, name='contact'),
    path('', index, name='index'),  # This makes the homepage point to the 'index' view
    path('menu/', menu, name='menu'),
]