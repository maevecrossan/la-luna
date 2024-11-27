# Manual Testing

## Development : Bugs and Fixes
| Issue | Details | Fix |
|-----|:-----:|:-----:|
| ![testing screenshot](photo-link) | While creating the admin panel, the date input was not rendering properly. | Register BookingAdmin model in admin.py |
| ![testing screenshot](photo-link) | Booking form fields not appearing. | ![testing screenshot](photo-link) Install cripsy forms and pass `form` into the bookingsystem views.py file. |
| ![testing screenshot](photo-link) | When preventing bookings in the past (date-wise), the date field stopped working completely. | ![testing screenshot](photo-link) Added `min="{{ today }}` |
| ![testing screenshot](photo-link) | ![testing screenshot](photo-link) Google dev tools raised 6 issues relating to my form fields not having ids. | ![testing screenshot](photo-link) Added ids to the `BookingForm` model |
| ![testing screenshot](photo-link) | Email.js and POST method conflicting: At times, only one function was being executed. When email.js was working, it tripped up the POST request, and vice versa. | After several rounds of refactoring and debugging, updating the url, and the return statement in `booking-confirmation-email.js`. |
| ![testing screenshot](photo-link) | issue | fix |

## Post Development : Bugs and Fixes