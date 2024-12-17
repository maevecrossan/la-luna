### **Agile Development Process**
#### **Overview** 

To track my development, I used Github Boards and followed Agile methodology. I gave each user story acceptance criteria which helped focus me and encouraged efficient progress towards the MVP.

Below is a table laying out the timeframe for each sprint. Following is a brief overview of each sprint. I limited each sprint by date, (rather than time) as it was most realistic with my schedule during developemt. 

*Any errors spoken about below will be included in the 'Bugs and Fixes' section of the TESTING.md file*

| Sprint Number | Duration | Completed |
| :--------: | :-------: | :-------: |
| 0 | dd/mm/yyyy |  |
| 1 | 18/11/2024 - 18/11/2024 | On Time |
| 2 | 19/11/2024 - 29/11/2024 | No |
| 3 | 30/11/2024 - 4/12/2024 | Early |
| 4 | 3/12/2024 - 8/12/2024 | On Time |
| 5 | 9/12/2024 - 9/12/2024 | On Time |
| 6 | 10/12/2024 - 10/12/2024 | On Time |


##### Sprint 0
Very early on I had began coding when I saw the project brief using Flask as a way to practice using the framework. Therefore, I consider my inital sprint everything I did up until I installed Django and fully understood the assignemnt brief.

During this stage, I also reviewed my user stories and decided to drop some.

**User Stories Dropped/Changed:**

* As a user, I can create a booking and receive a booking ID rather than create an account. 
* Googe maps API.
* Dynamic menu
* Admin users can respond to contact form messages in the dashboard.

----
##### Sprint 1
During this sprint I set up my project by completing the following:

* Installed Django
* Created the `bookingsystem` app.
* Prepared the project for Heroku deployment. 
* Connected the database and created the superuser.

*This sprit was completed in one day on November 18th.*

----

##### Sprint 2
During this sprint I was concerned with setting up the 'C' in CRUD in relation to the booking model. I would like to note that I am aware that this sprint was longer than it should have been and is a lesson I learned. I underestimated the work that this user story would require and defiently could have separated the tasks into more manageable, bite-size chunks. 

During this sprint, I planned on:

* Set up booking form. (No POST functionality at this time.)
    - Install cripsy forms.
    - Restrict times and dates on which users can make a booking.
    - Limit the capacity to 40 people. 
* Organise admin view for bookings (add filters).
* Update Flask links to Django format.
* Add active and expired check on bookings.
* Replace insecure Secret Key with hidden and secure one for deployment.

*This sprint was not completed on time due to form field and POST errors that took time to debug. The 'active/expired' check was pushed to the next sprint*

----

##### Sprint 3

During this sprint I was focused on:
1) completing incomplete tasks from the previous sprint,
2) building a html template for the user's 'my bookings' page
3) enabling users to create an account. 

I did this by:

* Adding 'active/expired' checks to bookings.
* Creating a html template to display bookings made by users. (Partially satisfied the 'R' aspect of CRUD, but all bookings were visible at once due to no AllAuth.)
* Installing AllAuth and linking AllAuth user pages (log-in,log-out and register pages) to the booking form. 
* Style AllAuth user pages. 
* Add user status to top right of header to show logged in status. 

*This sprint was completed a day early*

----

##### Sprint 4

During this sprint I was concerned with creating a `My Bookings` page through which users could perform the remaining ('R','U','D') CRUD functionality. 

I did this by:

* Filtering bookings so that only the user who made them could view them. 
* Add edit & delete buttons to bookings on the `My Bookings` page.
* Add delete button functionality. 
* Add delete confirmation modal.
* Add edit button functionality. 

Notes:
During this sprint, I noticed the POST functionality wasn't working as expected. The debugging for this was completed during this sprint. 

---- 

##### Sprint 5

During this sprint, I concerned myself with going back over the small pieces that I had missed or were not huge priorities during the previous sprints.

My tasks included:
* Updating the delete modal functionality so that it's only triggered when clicking the delete button. (Was previously being fired when 'edit' was being clicked.)
* Tidied up files to be PEP8 compliant.
* Updating styles to be consistent on all pages. 

----

##### Sprint 6

Given how quickly I had completed my MVP, I decided to extend my MVP to link the contact form to the admin page. This was originally categorised as a 'could have' feature.

During this sprint I also did some 'housekeeping' by removing out debugging prints, making files PEP8 complaint, as well as adjusting styles to make website more accessible. 

This sprint was wrapped up by the testing phase.

----
