# Manual Testing

## Development : Bugs and Fixes
| Issue | Details | Fix |
|-----|:-----:|:-----:|
| ![testing screenshot](docs/testing/date_field_not_working.png) | While creating the admin panel, the date input was not rendering properly for the admin. | ![testing screenshot](docs/testing/date_field_now_working_rearranged_and_imported_custom_form_to_admin.png) Register custom BookingAdmin model in admin.py |
| ![testing screenshot](docs/testing/form-fields-not-appearing.png) | Booking form fields not appearing. | ![testing screenshot](docs/testing/form-fields-appearing-1.png) ![testing screenshot](docs/testing/form-fields-appearing-2.png) Install cripsy forms and pass `form` into the bookingsystem views.py file. |
| ![testing screenshot](docs/testing/form-date-debug-1.png) ![testing screenshot](docs/testing/form-date-debug-2.png) | When preventing bookings in the past (date-wise), the date field stopped working completely. | ![testing screenshot](docs/testing/form-date-debug-3.png) Added `min="{{ today }}` |
| ![testing screenshot](docs/testing/no_id_for_form_inputs1.png) | ![testing screenshot](docs/testing/no_id_for_form_inputs2.png) ![testing screenshot](docs/testing/no_id_for_form_inputs3.png) Google dev tools raised 6 issues relating to my form fields not having ids. | ![testing screenshot](photo-link) Added ids to the `BookingForm` model |
| ![testing screenshot](docs/testing/form_not_posting_after_emailjs_bug_fixed1.png) | Email.js and POST method conflicting: At times, only one function was being executed. When email.js was working, it tripped up the POST request, and vice versa. | After several rounds of refactoring and debugging, updating the url, and the return statement in `booking-confirmation-email.js`. |
| ![testing screenshot](docs/testing/bookings_rendering_no_style.png) | Bookings previously only visible on backend now visible on front end but styling wasn't rendering and was very messy and unreadable. Validity was also incorrect. | Styling fixed to isolate bookings into a more appealing presentation. Validity just needed one simple tweak from <br>`return datetime.now() < end_datetime` to <br> `return datetime.now() > end_datetime` (line 150 bookingsystem/models.py) |
| ![testing screenshot](docs/testing/updated_runtime_file.png) | Issue deploying on Heroku. | I had forgotten to recollect my static files, so I did so which fixed the issue. During deploying, the logs stated I should update python for improved security. <br> I did so but had to rename my runtime.txt file to `.python-version` and merely state the numeric verion I wished to use. After removing the python prefix, the project successfully built and deployed.|
|  | One of my largest and reoccuring issues was to do with the `my-bookings` section appearing. The issue came to light when adding user authentication and filtering. The `my-bookings` page displayed the message for when there are no bookings, despite my database storing roughly 20 bookings at the time. In the end, the fix was relatively simple, but was tricky to initially find. | I originally allowed the user field (booking model) to have `blank` and `null` to be `true`, meaning bookings could be created (in early development) without a username. This was done so I could implement the booking system without encountering errors. By removing those two fields and migrating the changes to the database, the 'my-bookings' page correctly displayed bookings relevant to the signed-in user. |
| ![testing screenshot](docs/testing/mob_nav_not_appearing.png) | Mobile nav toggle not rendering after adding login status message in header. | ![testing screenshot](docs/testing/mob_nav_not_appearing2.png) Fixed stylings in CSS. (Nav toggle was later centered) |
| ![testing screenshot](docs/testing/expired_function_not_working_1.png) [testing screenshot](docs/testing/expired_function_not_working_2.png) | [testing screenshot](docs/testing/expired_function_working_1.png) [testing screenshot](docs/testing/expired_function_working_2.png) Another common issue I encountered was the expired function not working. All bookings were marked as active, despite being expired. | The function was not correctly calculating the end time for each booking, as so wasn't being flagged as expired as there was no `end_time` to compare to. I fixed this by changing `end_time` to `time`.|
| ![testing screenshot](docs/testing/edit_booking_not_working_1.png) | Edit booking button not working correctly. | ![testing screenshot](docs/testing/edit_booking_working.png) A simple replacement of the urls from `booking.html` to `my-bookings`. |
| ![testing screenshot](docs/testing/url_no_prefix.png) | Links to views not linking properly, causing errors and preventing pages from rendering. It also prohibited the POST function to execute properly. | Adding the `bookingsystem` prefix to the view names in the views.py file as well as the html file, allowing them to render properly. The POST function also began working as expected. |
| ![testing screenshot](docs/testing/delete_modal_working.png) | I ran into some difficulty when attempting to implement a deletion confirmation modal. This was largely due to me not including Bootstrap's JavaScript. | By adding the script file and moving `my-bookings-crud.js` back to the base.html file, the modal appeared correctly. I did have to alter the url attached to the modal delete button to contain the prefix mentioned in the previous fix. |
| ![testing screenshot](docs/testing/modal_on_edit_page.png) | An console error was appearing when editing a booking regarding the delete modal. | ![testing screenshot](docs/testing/modal_conditional.png) The modal was made conditional and was only to be triggered when it is present. |
| ![testing screenshot](docs/testing/edit_function_duplicating.png) | Rather than replacing the original booking with the updated version, the edit function creates a new booking with the updated version. | ![testing screenshot](docs/testing/form_action_before_and_after.png) The previous form action was overriding any editing logic. Once the form action was updated, bookings were successfully edited and updated and no additional bookings were made. |
|  | 500 error appearing submitting form after removing 'required' attribute in devtools from 'date' input field. | ![testing screenshot](docs/testing/date_field_update.png) ![testing screenshot](docs/testing/field_date_update_2.png) Add additional checks and validationin the models.py file and forms.py |
| ![testing screenshot](photo-link) | Issue | Fix |
| ![testing screenshot](photo-link) | Issue | Fix |
 
## Post Development Manual Testing

| **Test Category**     | **Test Case**                                                                 | **Expected Outcome**                                           | **Mobile** | **Desktop** |
|-----------------------|-------------------------------------------------------------------------------|----------------------------------------------------------------|------------|-------------|
| **Base Template Features** | Ensure navigation links work correctly.                                  | Buttons/links navigate to the correct pages.                   | Yes | Yes |
|                       | Ensure navigation collapses.                                                  | Navigation wraps on medium screens and collapses to a burger icon on smaller screens.   | Yes | Yes |
|                       | All footer Links work correctly.                                              | Directory links and SNS links work as expected.  | Yes | Yes |
|                       | Footer collapses correctly on smaller screens.                                | Columns wrap and stack on mobiles.  | Yes | Yes |
|                       |                                                 |   |  |  |
| **Homepage**          | Verify hero section content (text, images, alignment).                        | Content is accurate, properly aligned, and visually appealing.  | Yes | Yes |
|                       | Check 'Make Reservation' link.                                                | Links to 'Booking' page.  | Yes | Yes |
|                       | Our Story section appears correctly.                                          | Animations occur when link is pressed.  | Yes | Yes |
|                       | Gallery renders correctly.                                                    | Six images on desktop (3 x 2 rows), three on mobile (vertically centered).  | Yes | Yes |
|                       |                                                 |   |  |  |
| **Menu**              | Content is accurate, properly aligned, and visually appealing.                | Verify all dishes are listed with descriptions and pricing.  | Yes | Yes |
|                       | Content collapses and expands while maintaing visible.                        | Content should narrow or widen depending on screensize. | Yes | Yes |
|                       |                                                 |   |  |  |
| **My Bookings**       | If logged out, users should be promted to log in.                             | Sign in page appears.  | Yes | Yes |
|                       | If logged in, users should br brought to the booking form.                    | Form appears. | Yes | Yes |
|                       | My bookings link at top of booking form links to booking list page.           | My bookings page appears. | Yes | Yes |
|                       | Form won't submit with an empty field.                                        | Error message appears under the relevant field.  | Yes | Yes |
|                       | If 'required' is removed from html in devtools, form will still not submit.   | Error message appears under relevant field. | Yes | Yes |
|                       |                                                 |   |  |  |
| **Contact Form**      | All users (logged in and out) should be able to access and submit the form.   |   |  |  |
|                       |                                                 |   |  |  |
|                       |                                                 |   |  |  |








| **Booking Page**      | Test form field validations (e.g., email format, required fields).            | Error messages appear for invalid inputs; valid inputs submit correctly.|
|                       | Submit valid data and verify the success response.                           | Booking completes with confirmation message.                            |
|                       | Ensure the booking calendar prevents past-date selection.                    | Users cannot select dates in the past.                                  |
|                       | Test navigation back to the homepage from the booking page.                  | Navigation works correctly.                                             |
| **Services Page**     | Verify all services are listed with descriptions and pricing.                | Services display accurate details, pricing, and links (if any).         |
|                       | Test image and link functionality for each service.                          | Images load, and links navigate correctly.                              |
| **About Us Page**     | Check team details and static content accuracy.                              | All information is accurate and up to date.                             |
|                       | Test external links (e.g., social media profiles).                           | External links open in new tabs and lead to correct pages.              |
| **Contact Page**      | Test the contact form with valid/invalid inputs.                              | Invalid inputs trigger errors; valid inputs submit successfully.        |
|                       | Verify success/failure messages after form submission.                       | Users receive appropriate feedback after submission.                    |
|                       | Test phone numbers, email links, and embedded maps (if applicable).          | Phone/email links work, and maps load correctly.                        |
| **Login/Signup**      | Verify login with valid and invalid credentials.                              | Valid credentials log in; invalid ones display error messages.          |
|                       | Test account creation and password recovery flows.                           | Users can create accounts and reset passwords successfully.             |
| **Dashboard**         | Verify user-specific content after login.                                    | Logged-in users see the correct personalized content.                   |
|                       | Test logout functionality.                                                   | Logging out redirects users to the homepage or login page.              |
|                       | Ensure restricted pages redirect unauthenticated users to the login page.     | Users cannot access restricted pages without logging in.                |
| **End-to-End Flows**  | Start on the homepage, complete the booking flow, and verify confirmation.   | Users can successfully book and see confirmation.                      |
|                       | Navigate all pages via the menu and return to the homepage.                  | Navigation is seamless and functional.                                  |
|                       | Submit all forms with empty, invalid, and valid inputs.                      | Forms validate correctly and provide appropriate feedback.              |
|                       | Test error handling for 404 or server errors.                                | Users see a friendly error page for invalid URLs or server issues.      |



### Logged in Testing


### Logged Out Testing


### Admin Testing



### Bugs and Fixes

### Manual Testing