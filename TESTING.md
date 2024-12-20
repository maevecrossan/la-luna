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
| ![testing screenshot](docs/testing/empty_guest_field_500_error.png) | Submitting blank guests input brings user to 500 error page rather than triggering error message. | ![testing screenshot](docs/testing/empty_field_error_fix.png) Added additional check to prevent 500 page from appearing. |
| ![testing screenshot](docs/testing/email_error.png) ![testing screenshot](docs/testing/email_error_2.png) | Confirmation email sending not working. | After several hours of debugging (trying old code, reinstalling the feature, asking ChatGPT, and trying Django's email alternative) no emails were being sent upon booking form submission. After trying to fix it to no avail, and as it is not a requirement for this project, I decided to remove the feature and to include it at a later time. I have included two screenshots. The first is my terminal which shows the app working as expected with no errors. The second is an emial that successfully sent 24 hours before the time of writing this. In an attempt to save time (and my sanity), I will attempt to implement it in a future iteration. |

 
## Post Development Testing

| **Test Category**     | **Test Case**                                                                 | **Expected Outcome**                                           | **Mobile** | **Desktop** |
|-----------------------|-------------------------------------------------------------------------------|----------------------------------------------------------------|------------|-------------|
| **Base Template Features** | Ensure navigation links work correctly.                                  | Links navigate to the correct pages.                   | Yes | Yes |
|                       | Test end-to-end flows.                                                        | All pages work and link correctly when accessed from one another.  | Yes | Yes |
|                       | Ensure navigation collapses.                                                  | Navigation wraps on medium screens and collapses to a burger icon on smaller screens.   | Yes | Yes |
|                       | All footer Links work correctly.                                              | Directory links and SNS links are present and work as expected.  | Yes | Yes |
|                       | Footer collapses correctly on smaller screens.                                | Columns wrap and stack on mobiles.  | Yes | - |
|                       | Nav dropdown appears.                                                         | If a user is authenticated, they will be able to access the booking dropdown. Otherwise they will only see 'Bookings' and will be promted to sign in. | Yes | Yes |
| **Homepage**          | Hero section behaves correctly.                                               | Hero section resizes and remains centered on smaller screens. Test remains visible.  | Yes | Yes |
|                       | Hero 'make reservation' button behaves correctly.                             | Links to booking page. Prompts unauthorised users to sign in. Bring authorised users to booking form. | Yes | Yes |
|                       | Our Story section animates correctly.                                         | Animations occur when link is pressed. | Yes | Yes |
|                       | Our Story section appears as expected.                                        | Renders correctly on an already loaded page. | Yes | Yes |
|                       | Our Story section resizes as expected.                                        | Collapses while remaining readable on smaller screens. Remains centered on larger screens. | Yes | Yes |
|                       | Gallery renders correctly on large screens.                                   | Six images on desktop (3 x 2) | - | Yes |
|                       | Gallery renders correctly on medium/tablet screens.                           | Three images stacked vertically. | Yes | Yes |
|                       | Gallery renders correctly on small screens.                                   | Three images stacked vertically. | Yes | - |
|                       |                                                 |   |  |  |
| **Menu**              | Content is accurate, properly aligned, and visually appealing.                | Verify all dishes are listed with descriptions and pricing.  | Yes | Yes |
|                       | Content collapses and expands while maintaing visible.                        | Content should narrow or widen depending on screensize. | Yes | Yes |
|                       |                                                 |   |  |  |
| **Booking Form**       | If logged out, users should be promted to log in.                             | Sign in page appears. Unauthorised users cannot make bookings. | Yes | Yes |
|                       | If logged in, users should br brought to the booking form.                    | Form appears. | Yes | Yes |
|                       | My bookings link at top of booking form links to booking list page.           | My bookings page appears. | Yes | Yes |
|                       | Form won't submit with an empty field.                                        | Error message appears on top of form and under relevant field. Custom 500 page as fallback. Form will not submit with an empty field. | Yes | Yes |
|                       | Remove 'required' attribute in devtools and try submit with an empty field.   | Form will not submit. Custom error message appears on top of form and under relevant field. Custom 500 page as fallback. | Yes | Yes |
|                       | Enter invalid information in each field.                                      | Django error message appears on top of form and under relevant field. The form will not submit.| Yes | Yes |
|                       | Submit valid data and test for success response.                              | User will be redirected to 'my bookings' page and see a success message below the heading. | Yes | Yes |
|                       | Correct promt heading is displayed when creating a new booking.               | 'Book with us today!' is displayed at the top of the form. | Yes | Yes |
|                       | Correct submit button is displayed when creating a new booking.               | 'Make reservation' is displayed on the button. | Yes | Yes |
|                       | User is redirected after submitting a valid booking.                          | User is redirected to the 'My Bookings' page where they can view their booking. | Yes | Yes |
|                       |                                                 |  |  |  |
|   **My Bookings**     | User has no bookings.                                                         | User will see a message promting them to make a booking. A clickable link will direct them to the booking form. | Yes | Yes |
|                       | User has bookings. | Valid bookings will be displayed under the 'Upcoming Bookings' section, while 'Expired bookings' display bookings that have passed the current date and time combination. | Yes | Yes |
|                       | User can click the edit button and modify their booking.                      | Details are updated. User is redirected to My Bookings page. Success message appears. | Yes | Yes |
|                       | User can click the edit button and modify expired bookings.                   | User will have to update the date or an error will appear. If date is valid, details are updated. User is redirected to My Bookings page. Success message appears. | Yes | Yes |
|                       | User can delete a booking (valid and expired).                                | A confirmation modal appears to check if the user is sure. 'Close' cancels the action. 'Delete' removes the booking from the database and fromthe My Bookings page. Deleted message appears on the refreshed page. | Yes | Yes |
|                       |                                                 |  |  |  |
| **Contact Form**      | All users (logged in and out) should be able to access and submit the form.   | - | Yes | Yes |
|                       | Form won't submit with an empty field.                                        | Django error message appears on top of form and under relevant field. Custom 500 page as fallback. | Yes | Yes |
|                       | Remove 'required' attribute in devtools and try submit.                       | Form will not submit. Custom error message appears on top of form and under relevant field. Custom 500 page as fallback. | Yes | Yes |
|                       | Enter invalid information in each field.                                      | Django error message appears on top of form and under relevant field. The form will not submit. | Yes | Yes |
|                       | Submit valid data and test for success response.                              | User will see a success message above the form. | Yes | Yes |
|                       |                                                 |  |  |  |
| **Login/Signup/Logout** | Attempt login with invalid credentials.                                     | Invalid credentials or form inputs will display error messages.          | Yes | Yes |
|                       | Attempt login with valid credentials.                                         | Successful sign in.          | Yes | Yes |
|                       | Test account creation with invalid info.                                      | Invalid form inputs will display error messages.             | Yes | Yes |
|                       | Test account creation with valid info.                                        | User can create account.             | Yes | Yes |
|                       | Test logout functionality.                                                    | User can click the confirm button on confirmation page. Logging out redirects users to the homepage or login page.              | Yes | Yes |
|                       |                                                 |  |  |  |
| **Admin Dashboard**   | Users verified by super user can access admin panel.                          | Users verified as 'staff' will have access to the admin panel.           | - | Yes |
|                       | Admin only accessible by adding `/admin` manually to the end of the homepage link.| No links on the customer-user page to suggest access to the database/dashboard for security. |  |  |
|                       | Regular users cannot sign in to the admin panel.                              | Users cannot access restricted pages unless verified by the super user. | - | Yes |
|                       | Dashboard users can organise bookings with various filters.                   | Bookings can be organised by name, date, validity, etc. | - | Yes |
|                       | Dashboard users can view contact form submissions.                            | Contact form submissions can be view as a list but also clicked into to view the information submitted more clearly. | - | Yes |
|                       | Dashboard users can mass delete selected booking or contact form submissions. | Users can select and delete selected bookings from the `action` drop down menu. | - | Yes |
|                       | Dashboard users can see user information (user names, reigstered emails, but never passwords).| - | - | Yes |
|                       | Dashboard users can delete a user from the database.                          | Cascading setting will delete all traces of that user and their booking(s). | - | Yes |

## Responsiveness Tests

'Am I responsive?' was used to illustrate the ways in which each page scales down/changes depending on the screensize. Below are screenshots of each feature on the respective pages, with an additional screenshot taken on a phone view as I find the 'Am I responsive?' phone mock-up to be slightly inaccurate.

(Some pages that require being signed in are not accessible through Am I Responsive, in which case three screenshots taken across a phone, tablet and desktop will be included.)

* [Nav Am I Responsive](docs/testing/responsive-tests/air_nav.png)
* [Nav Am I Responsive Mobile Screenshot](docs/testing/responsive-tests/air_nav_mobile.jpeg)

* [Footer Am I Responsive](docs/testing/responsive-tests/air_footer.png)
* [Footer Am I Responsive Mobile Screenshot](docs/testing/responsive-tests/air_footer_mobile.jpeg)

* [Hero Am I Responsive](docs/testing/responsive-tests/air_hero.png)
* [Hero Am I Responsive Mobile Screenshot](docs/testing/responsive-tests/air_hero_mobile.jpeg)

* [Our Story Am I Responsive](docs/testing/responsive-tests/air_our_story.png)
* [Our Story Am I Responsive Mobile Screenshot](docs/testing/responsive-tests/air_our_story_mobile.jpeg)

* [Gallery Am I Responsive](docs/testing/responsive-tests/air_gallery.png)
* [Gallery Am I Responsive Mobile Screenshot](docs/testing/responsive-tests/air_gallery_mobile.jpeg)

* [Menu Am I Responsive](docs/testing/responsive-tests/air_menu.png)
* [Menu Am I Responsive Mobile Screenshot](docs/testing/responsive-tests/air_menu_mobile.PNG)

* [Booking Form Am I Responsive Desktop Screenshot](docs/testing/responsive-tests/air_booking_form_desktop.png)
* [Booking Form Am I Responsive Tablet Screenshot](docs/testing/responsive-tests/air_booking_form_tablet.jpeg)
* [Booking Form Am I Responsive Mobile Screenshot](docs/testing/responsive-tests/air_booking_form_mobile.PNG)

* [My Bookings Am I Responsive Desktop Screenshot](docs/testing/responsive-tests/air_my_bookings_list_desktop.png)
* [My Bookings Am I Responsive Tablet Screenshot](docs/testing/responsive-tests/air_my_bookings_list_tablet.jpeg)
* [My Bookings Am I Responsive Mobile Screenshot](docs/testing/responsive-tests/air_my_bookings_list_mobile.jpeg)

* [Edit Booking Am I Responsive Desktop Screenshot](docs/testing/responsive-tests/air_edit_desktop.jpeg)
* [Edit Booking Am I Responsive Tablet Screenshot](docs/testing/responsive-tests/air_edit_tablet.jpeg)
* [Edit Booking Am I Responsive Mobile Screenshot](docs/testing/responsive-tests/air_edit_mobile.jpeg)

* [Delete Booking Confirmation Am I Responsive Desktop Screenshot](docs/testing/responsive-tests)
* [Delete Booking Confirmation Am I Responsive Tablet Screenshot](docs/testing/responsive-tests)
* [Delete Booking Confirmation Am I Responsive Mobile Screenshot](docs/testing/responsive-tests)

* [Contact Form Am I Responsive](docs/testing/responsive-tests)
* [Contact Form Am I Responsive Mobile Screenshot](docs/testing/responsive-tests)

* [Sign In Am I Responsive](docs/testing/responsive-tests/air_sign_in.png)
* [Sign In Am I Responsive Mobile Screenshot](docs/testing/responsive-tests/air_sign_in_mobile.PNG)

* [Sign Up Am I Responsive](docs/testing/responsive-tests/air_sign_up.png)
* [Sign Up Am I Responsive Mobile Screenshot](docs/testing/responsive-tests/air_signup_mobile.jpeg)

* [Log Out Confirmation Am I Responsive  Desktop Screenshot](docs/testing/responsive-tests/air_signout_desktop.png)
* [Log Out Confirmation Am I Responsive Tablet Screenshot](docs/testing/responsive-tests/air_signout_tablet.PNG)
* [Log Out Confirmation Am I Responsive Mobile Screenshot](docs/testing/responsive-tests/air_signout_mobile.PNG)

* [404/500 Error Page Am I Responsive](docs/testing/responsive-tests)
* [404/500 Error Page Am I Responsive Mobile Screenshot](docs/testing/responsive-tests)

## Eight Shapes Contrast Grid

Below is a screenshot of how I ensured my colour combinations passed the contrast test so the website remains accessible to all users. No combinations labelled DNP were used for essential aspects such as text, but may have been used for box borders, accents, etc.

![Colour Contrast Grid](docs/testing/colour-contrast-test.png)

## WAVE Evaluation Tool

## Lighthouse

## PEP8

## JavaScript

## HTML

