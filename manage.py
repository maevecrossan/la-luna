#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import json
from flask import Flask, render_template, request, flash


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'laluna.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


app = Flask(__name__, static_url_path='/static', static_folder='static')


if __name__ == '__main__':
    main()


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/menu")
def menu(): # view is called inside html file
    return render_template("menu.html", page_title="Menu")


@app.route("/bookings")
def bookings(): # view is called inside html file
    return render_template("bookings.html", page_title="Bookings")


@app.route("/bookings", methods=['POST'])
def handle_booking():
    # Handle the booking here
    return 'Booking received!'


@app.route("/contact")
def contact(): # view is called inside html file
    return render_template("contact.html", page_title="Contact Us")


