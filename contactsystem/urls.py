from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact_system, name='contact'),
]