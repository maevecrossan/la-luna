import os
import json
from flask import Flask, render_template, request, flash

app = Flask(__name__) 
app = Flask(__name__, static_url_path='/static', static_folder='static')


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


if __name__ == "__main__": #__main__ is the default module in python
    app.run( # we want to run our app using the arguments inside this statement
        host=os.environ.get("IP", "0.0.0.0"), 
        port=int(os.environ.get("PORT", "5000")),
        debug=True #SHOULD ONLY BE TRUE IN DEVELOPMENT. CHANGE TO FALSE BE SUBMITTING.
    )