# **La Luna**
## **Introduction**
Welcome to La Luna, the online gateway to an exceptional fine-dining experience. Designed to reflect the elegance and sophistication of the restaurant itself, this website ensures that every visitor’s journey—from exploring our offerings to reserving a table—is as delightful and seamless as the dining experience at La Luna.

## **Table of Contents**



# **Planning**

## Strategy

### Site Aims

The aim of this webiste was to provide a sleek, intuitive experience for users who wish to learn about the La Luna restaurant, make a reservation, and ask questions. 

Users would be able to create an account through which they can create, edit and modify bookings. Admin users could also keep track of bookings through the admin dashboard.

### Opportunities

Below are the main points that arose when planning my project. The scores given to each opportunity were influences by the project timeframe, familiarity with the languages and frameworks used, and project scope.

Opportunity | Importance | Viability/Feasibility
---|:---:|:---:|
Learn about restaurant history | 4 | 5
See images of the restaurant | 3 | 5
Display a menu with all relevant details | 5 | 5
Allow menu to be edited and updated by admin | 1 | 1
Display contact info | 5 | 5
Create an account to keep to track of bookings | 5 | 5
Give bookings 'active/expired' labels for better UX | 5 | 5
Allow users to create, edit and delete bookings | 5 | 5
Allow users to make multiple bookings | 5 | 5
Allow uses to access social media links | 4 | 5
Users can send a message via a contact form | 4 | 5
Display a map of the location | 2 | 2 
Allow admin to add and remove items from the menu | 2 | 2
Create an a newsletter to be distributed to account holders | 1 | 2
Allow users to make a booking without creating an account. | 1 | 1
Allow admin users to view and filter bookings made by users. | 5 | 5
Allow admin users to view and filter contact form submissions. | 5 | 5
Allow admin users to respond to respond to contact form messages in the dashboard. | 3 | 1
Restrict capacity to 40 people at any one time | 5 | 5
Add a review section for registered customers. | 1 | 2
Google Maps API. | 1 | 1
---------- | --- | ---
**TOTAL** | **72** | **77**


## Scope

I divided these opportunities into categories under the MoSCoW headings for clarity.

* Must Have:
    * See a full menu with allergens.
    * See the history of the establishment.
    * See contact info.
    * Instantly make a booking and see what times and dates are available for bookings.
    * Instantly modify a booking.
    * Instantly delete a booking.
    * Make multiple bookings.
    * Create an account to keep track of bookings.
    * Admin can view and filter bookings made by users.
    * 40 people capacity.

* Should Have:
    * View images of the restaurant so I know what the atmosphere is like.
    * Have social media links easily accessible.

* Could Have:
    * Send a message to the restaurant staff if I have a query.
    * Dynamic menu.
    * Allow menu to be updated by staff.
    * Admin users can respond to contact form messages in the dashboard.

* Won't Have:
    * Review section.
    * Allow users to create and modify bookings without creating an account by having a booking ID.
    * Google Maps API.
    * Newsletter distribution.

## Structure

### User Stories

As a user...
* I want to experience an intuitively laid-out website.
* I want to see images so I know what atmosphere to expect.
* I want to create an account to keep track of my bookings.
* I want to make, edit, and delete bookings without contacting the restaurant directly.
* I don't want to be able to make reservations on days when they are closed or past closing hours. 
* I want to be able to contact the restaurant by phone, email, and message through their website.
* I want to easily access social media links from each page.
* I want to easily access contact information from each page.
* I want to learn about the restaurant's history.
* I want to view a menu with prices and any relevant allergens.

As a manager/owner...
* I want to provide a clutter-free website so customers aren't overwhelmed.
* I want to convey the 'vibe' of the establishment via images on the homepage so users know what to expect.
* I want to display a menu with allergen information and prices. 
* I want to allow users to create an account.
* I want users to have full control over bookings through said account so that staff can prioritise their time.
* I want users to know that tables will be given for two hours.
* I want users to have several means of contacting the restaurant (contact form, phone number, email). 
* I want users to not make reservations for more than 8 people via the booking form.
* I want an admin page where view bookings, user account details, and contact form submissions.
* I want users to have access to our social media pages via the footer.
* I want users to have access to our contact details via the footer. 
* I want users to be able to learn about the history of the establishment on the homepage.
* I want staff to be able to access all form submissions via the admin page.
* I want staff to be able to see a list of bookings made and to be able to organise them by different criteria (validity, name, date, etc).
* I want staff to be able to see a list of contact form submissions. (The details of which can be copied and replied to using the company email account.)


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

## **Skeleton**
### Wireframes
* [Homepage wireframes](docs/wireframes/homepage_wireframe.png)
* [Menu wireframe](docs/wireframes/menu_wireframe.png)
* [Bookings wireframe](docs/wireframes/booking_form_wireframe.png)
* [My Bookings wireframe](docs/wireframes/booking_list_wireframe.png)
* [Homepage wireframe](docs/wireframes/menu_wireframe.png)

The 'Our Story' section deisgn wasn't confirmed at this point as I wanted to make the list appear in a dynamic way and some character to the page. 

### Database

Below is the ERD for my database schema. I opted to user the default user model from the AllAuth library.

The most extensive model is by far the booking model, that required user validation before accessing the form. 
The contact model behaves in isolation and behaves separarely from the booking model.

![Database ERD](docs/database-erd/models.png)

## **Surface**
* Colors
* Fonts
* Images

## **Features**
### **Base**
* Logo
* Nav (hamburger)
* Content
* Footer
* Account features & status

### **Index/Home**

### **Menu**

### **My Bookings**


#### **My bookings list (via form)**


### **Our Story**

### **Gallery**

### **Contact Us**

## **Future Development**

## **Testing**

## **Deployment**

## **Tech used**

## **Credits**

### **Resources**