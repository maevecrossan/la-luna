from django.shortcuts import render


def index(request):
    return render(request, '../templates/index.html')


def menu(request):
    return render(request, '../templates/menu.html')


def contact(request):
    return render(request, '../templates/contact.html')