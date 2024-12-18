# **La Luna**

## **Introduction**
Welcome to La Luna, the online gateway to an exceptional fine-dining experience. Designed to reflect the elegance and sophistication of the restaurant itself, this website ensures that every visitor’s journey—from exploring our offerings to reserving a table—is as delightful and seamless as the dining experience at La Luna.

![La Luna Am I Repsonsive Screenshot](docs/testing/am_i_responsive_test_home.png)

## **Table of Contents**



## **Planning**

### Strategy

#### Site Aims

The aim of this webiste was to provide a sleek, intuitive experience for users who wish to learn about the La Luna restaurant, make a reservation, and ask questions. 

Users would be able to create an account through which they can create, edit and modify bookings. Admin users could also keep track of bookings through the admin dashboard.

#### Opportunities

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


### Scope

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

### Structure

#### User Stories

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



### **Skeleton**
#### Wireframes
* [Homepage wireframes](docs/wireframes/homepage_wireframe.png)
* [Menu wireframe](docs/wireframes/menu_wireframe.png)
* [Bookings wireframe](docs/wireframes/booking_form_wireframe.png)
* [My Bookings wireframe](docs/wireframes/booking_list_wireframe.png)
* [Homepage wireframe](docs/wireframes/menu_wireframe.png)

The 'Our Story' section deisgn wasn't confirmed at this point as I wanted to make the list appear in a dynamic way and some character to the page. 

#### Database

Below is the ERD for my database schema. I opted to user the default user model from the AllAuth library.

The most extensive model is by far the booking model, that required user validation before accessing the form. 
The contact model behaves in isolation and behaves separarely from the booking model.

![Database ERD](docs/database-erd/models.png)

### **Surface**
#### Colour Scheme

Below is my colour scheme.

![Website colour scheme.](docs/surface/colour-palette.png)

**Fonts**

The fonts used in my project are from Google Fonts.

'Italiana' was used for decorative, large text. Lato was used for smaller text and longer sentences so that the user has no difficulty reading it.


**Images**

Below are the images I used for the hero image and in the gallery section. 

**Hero Image:**
* [Hero image: Two men standing behind the bar of an open restaurant.](https://images.pexels.com/photos/5490933/pexels-photo-5490933.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2)

**Gallery Images:**
* [Gallery image: A man working in a restaurant kitchen.](https://images.pexels.com/photos/14410382/pexels-photo-14410382.jpeg)
* [Gallery image: Two people clinking glasses.](https://images.pexels.com/photos/4255489/pexels-photo-4255489.jpeg)
* [Gallery image: Pasta being cut with a machine.](https://images.pexels.com/photos/4252785/pexels-photo-4252785.jpeg)
* [Gallery image: Uplcose shot of pepperoni pizza.](https://images.pexels.com/photos/20844860/pexels-photo-20844860/free-photo-of-pizza-served-in-a-restaurant.jpeg)
* [Gallery image: A man sprinkling flour on freshly cut pasta.](https://images.pexels.com/photos/4252779/pexels-photo-4252779.jpeg)
* [Gallery image: Hands clapping to remove flour.](https://images.pexels.com/photos/784633/pexels-photo-784633.jpeg)

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