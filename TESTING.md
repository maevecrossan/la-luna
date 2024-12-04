# Manual Testing

## Development : Bugs and Fixes
| Issue | Details | Fix |
|-----|:-----:|:-----:|
| ![testing screenshot](photo-link) | While creating the admin panel, the date input was not rendering properly. | Register BookingAdmin model in admin.py |
| ![testing screenshot](photo-link) | Booking form fields not appearing. | ![testing screenshot](photo-link) Install cripsy forms and pass `form` into the bookingsystem views.py file. |
| ![testing screenshot](photo-link) | When preventing bookings in the past (date-wise), the date field stopped working completely. | ![testing screenshot](photo-link) Added `min="{{ today }}` |
| ![testing screenshot](photo-link) | ![testing screenshot](photo-link) Google dev tools raised 6 issues relating to my form fields not having ids. | ![testing screenshot](photo-link) Added ids to the `BookingForm` model |
| ![testing screenshot](photo-link) | Email.js and POST method conflicting: At times, only one function was being executed. When email.js was working, it tripped up the POST request, and vice versa. | After several rounds of refactoring and debugging, updating the url, and the return statement in `booking-confirmation-email.js`. |
| ![testing screenshot](photo-link) | Bookings previously only visible on backend now visible on front end but styling wasn't rendering and was very messy and unreadable. Validity was also incorrect. | Styling fixed to isolate bookings into a more appealing presentation. Validity just needed one simple tweak from <br>`return datetime.now() < end_datetime` to <br> `return datetime.now() > end_datetime` (line 150 bookingsystem/models.py) |
| ![testing screenshot](photo-link) | Issue deploying on Heroku. | I had forgotten to recollect my static files, so I did so which fixed the issue. During deploying, the logs stated I should update python for improved security. <br> I did so but had to rename my runtime.txt file to `.python-version` and merely state the numeric verion I wished to use. After removing the python prefix, the project successfully built and deployed.|
| ![testing screenshot](photo-link) | One of my largest and reoccuring issues was to do with the 'my-bookings' section appearing. In the end, the fix was relatively simple, but was tricky for me to find. | I originally allow the user field to have 'blank' and 'null' and true, meaning bookings could be created (in early development) without a username. This was done so I could implement the booking system without ecountering error. By removing those two fields, the 'my-bookings' page displayed bookings relevant to the signed-in user. |
| ![testing screenshot](photo-link) | Mobile navigation not rendering after adding login status message in header. | Fixed stylings in CSS. |
| ![testing screenshot](photo-link) | Another common issue I encountered was the expired function not working. All bookings were marked as active, despite being expired. | The function was not correctly calculating the end time for each booking, as so wasn't being flagged as expired as there was no `end_time` to compare to. I fixed this by changing `end_time` to `time`.|
| ![testing screenshot](photo-link) | Issue | Fix |
| ![testing screenshot](photo-link) | Issue | Fix |
| ![testing screenshot](photo-link) | Issue | Fix |
| ![testing screenshot](photo-link) | Issue | Fix |
| ![testing screenshot](photo-link) | Issue | Fix |
| ![testing screenshot](photo-link) | Issue | Fix |
 
## Post Development : Bugs and Fixes