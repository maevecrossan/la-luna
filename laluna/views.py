"""
Defines project-level views.
"""

from django.shortcuts import render


def index(request):
    """
    View for index.html page.
    """
    return render(request, '../templates/index.html')


def menu(request):
    """
    View for menu.html page.
    """
    return render(request, '../templates/menu.html')
