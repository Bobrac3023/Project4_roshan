
# PROJECT4_ROSHAN - The Soul of India

## Introduction

The name “Mai” means “Mother” in the Marathi language — spoken in the state of Maharashtra, a large and culturally rich region in western India. Maharashtra is renowned for its mouth-watering cuisine that delights the senses and nourishes the soul.

Mai’s Kitchen is a tribute to this culinary heritage, offering patrons an authentic taste of Maharashtrian flavors in a modern dining experience.

## Project Summary

This project is a Django-based restaurant reservation system built for "Mai's Kitchen".

- Design Philosophy
  - Built using the Agile methodology with iterative enhancements and user feedback
  - Designed with a responsive layout, optimized for both mobile and desktop users

- Project Overview
  - It follows Django's MVT (Model-View-Template) architecture that enables customers to:
    - View homepage content and reviews.
    - Make table reservations online
    - View their upcoming reservations
    - Update or cancel their bookings as needed
    - Submit feedback. ( with and without login)
    - View contact info. ( embedded google map , email,contact number and timing)

  - It includes:
    - HTML templates for various pages.
    - Django models for Reservation and Feedback.
    - Forms to submit reservations and feedback.
    - Views for form handling, CRUD operations, and displaying data.

- Templates (HTML)
  - base.html: Master layout (header, footer)
  - index.html: Homepage
  - about.html: Feedback form
  - contact.html: Contact and map
  - reservation_form.html: reservation form
  - reservation_list.html: Display reservations made by the logged in  user
  - update_reservation.html: Edit form that helps logged in user update their own reservation
  - confirm_delete.html: Delete a users own reservations after login
  - 

- Models 
  - Reservation: Stores booking info, ensures rules (no past date, max 10 guests)
  - Feedback: Stores messages tied to reservation or user

- Views
  - PostList: Shows homepage
  - about_me: Saves or shows feedback
  - contact_us: Displays contact info
  - reservation_form: Save reservations after validation
  - update_reservation: Let user edit their own reservations
  - delete_reservation: Confirm and delete a users own reservations
  - reservation_list: Display user’s rservations only

- URLs 
  - /       → Home (PostList)
  - /about/ → Feedback (about_me)
  - /contact/       → Contact info
  - /reservation/form/ → Reservation form
  - /reservation/list/ → View Reservations
  - /reservation/update/ID → Edit reservations
  - /reservation/confirm_delete/ID → Delete reservations

- Forms 
  - ReservationForm: Collects name, email, time, date, guests
  - FeedbackForm: Collects guest/user opinion

### Logic Explained 

- Each step below shows what the user sees or can do:
  - Homepage: This is where users start. It shows information about the restaurant.
  - Login / Signup: Required before making any reservations.
  - Make a Reservation: Form is displayed only after login. Requires date, time, guests.
  - View My Reservations: Displays all bookings created by the logged in user.
  - Edit Reservation: Allows the logged in user to change date/time of their booking.
  - Delete Reservation: Lets the logged in user cancel their booking after confirmation.
  - Feedback: Open to all. Logged-in users link it to their booking.
  - Contact Page: Public page showing contact information and map.

## Features

- Core Feature  
  - Online Reservation System
    - Users can book a table with their name, email, date, time, guest count, and a message.
  - Form validations ensure:
    - No past dates allowed
    - Guest count must be between 1 and 10
    - Reservations are saved to the database and associated with the logged-in user if authenticated.

  - Update & Cancel Reservations
    - Logged-in users can:
      - Edit existing reservations (date, time, guests, etc.)
      - Cancel/delete reservations with confirmation prompts
      - Access to these views is protected with @login_required for security.

  - Feedback Submission
    - Any visitor (guest or registered user) can leave feedback
    - Feedback is stored and shown on the “About” page
    - If logged in, the feedback is attributed to the user

  - Reservation List Dashboard
    - Logged-in users can view a personalized list of all their reservations
    - Reservation statuses (e.g., “Requested”, “Confirmed”) are clearly shown
    - Options to update or delete directly from the table

  - Contact & Location Page
    - Displays the restaurant's physical location using an embedded Google Map
    - Shows operating hours, email address, and phone number

  - User Authentication
    - Integrated with django-allauth to support:
      - Sign up
      - Login
      - Logout
    - Protected views like “reservation list”, “update”, and “delete” are restricted to logged-in users

- Security and Validation.
  - CSRF protection included in all forms.
  - ***@login_required*** decorator,a built-in Django tool used to restrict access to certain views unless the user is authenticated applied above function-based view (FBV)
  - Login required for updating, deleting, and viewing reservations.
  - Model-level validation to prevent past dates and excessive guests.
  - Feedback can be submitted anonymously or by logged-in users.
- DRY - “Don’t Repeat Yourself”, software development principle to minimize code duplication and centralize logic deployed
  - Reusable Forms with Django’s ModelForm
  - Template Inheritance - A single base.html file defines the common layout (header, footer, Bootstrap inclusion, etc.), which is extended by all other templates using ***{% extends "base.html" %}***
  - Reusable Views and Logic
    - Using ListView for the homepage (PostList) to list reservations.
    - Wrap views (ike update/delete) with ***@login_required***, reducing the need to write authentication checks manually.
    - Validate model rules (e.g., date/time restrictions, guest limits) using clean() in the Reservation model, so that the logic is reused automatically in all views and forms.
  - Centralized Validation Logic
    - All business rules (like ensuring the reservation isn’t in the past and guest limits are respected) are placed inside the clean() method of the Reservation model. This means whether data comes from the admin panel, the form, or a script — the same validation applies universally.
- Mobile-Friendly & Responsive UI
  - Uses Bootstrap and Crispy Forms for:
    - Clean, responsive forms
    - Mobile-first design
    - Stylish layout with minimal effort
    - CSS media queries for different screen sizes.
- Admin Panel Integration
  - Reservations and feedback entries are accessible in Django’s admin interface
  - Admins can review, update, or moderate user submissions
- Footer Layout  
  - Social Media  
    - External links to Facebook, X(formerly twitter),Linkedin,Instagram, and Youtube pages in the website footer.
    - Each link configured to open in a new tab.
    - "Hover" property to hightlight social media icons.
  - Menu.
    - External link to download the menu in a PDF format.
- Others
  - Choice of foreground and background colors provide right contrast for a rich UI/UX experience .  
  - Aria accessibility for screen readers.
  - "Read More" buttons under "highlights section" of home page open in to external links. 

## Website Structure and feature description 

### HTML File Breakdown

- Base.html 
  - Purpose : The Template Foundation-Master Layout
    - The navigation bar (menu at the top)
    - Footer (social media links and copyright)
    - Common design (fonts, colors, CSS, JavaScript)
    - The {% block content %} section where other pages add their unique content

- index.html - the Homepage.
  - Purpose :  Show off the restaurant
    - Shows a big welcome message (jumbotron)
    - Has a "Reserve Now" button that displays a popup modal for login/signup
    - Shows View/Update/Delete Reservation buttons
    - Displays Customer reviews and Restaurant highlights
  - Who can view this?
    - Everyone. No login needed.

![homepage.png](readme.doc/homepage.png)

- about.html
  - Purpose :Page for users to leave and view feedback.
    - Lets guests and logged in users submit feedback
    - Shows past feedback messages (with name and time)
  - Who can view this?
    - Everyone. No login needed.

![about_page.png](readme.doc/about_page.png)

- contact.html
  - Purpose : Shows location and contact info of the restaurant.
    - Shows Google Map of Abu Dhabi location
    - Provides contact details like phone, email, timings
  - Who can view this?
    - Everyone. No login needed.

![contact_us_page.png](readme.doc/contact_us_page.png)

- reservation_form.html	
  - Purpose: Page to fill out a reservation form.
    - Simple form using Django’s crispy formatting
    - Collects user info and saves it when submitted
  - Who can view this?
    - Only logged in users

![reservation_form.png](readme.doc/reservation_form.png)

- reservation_list.html	
  - Purpose: Show a list of reservations for the logged-in user.
    - Displays all reservations made by the logged-in user.
    - If there are reservations, it shows them in a table
    - If not, it says “You have no reservations yet.”
    - Buttons to update or delete each reservation 
  - Who can view this?
    - Only logged in users

![reservation_list_success.png](readme.doc/reservation_list_success.png)

- update_reservation.html	
  - Purpose: Allows user to edit a reservation.
    - Shows a form with current reservation details
    - Lets you change the date, time, guest count, etc. 
  - Who can view this?
    - Only logged in users
  
- confirm_delete.html	
  - Purpose: Confirmation page before deleting a reservation.
    - Confirms cancellation before deleting a reservation.
    - Asks: “Are you sure you want to cancel?”
    - Offers "Yes" (delete) and "No" (go back) buttons
  - Who can view this?
    - Only logged in users

## Schema used for this Project

- Backend Logic (Python Files)
  - models.py (Database Schema) - 
    - Defines how Django stores, validates, and manages application data in the database.
    - This project contains two models:
    - Reservation Model: 
      - Stores name, email, date, time, guest count, and optional message. 
      - Includes: Validation to block past dates & Guest limits between 1 and 10
    - Feedback Model: 
    - Links to a reservation or user and stores feedback content

- forms.py (User Input)
  - Abstracts user input logic and applies consistent client-side + server-side validation.
  - ReservationForm:
    - Custom time slot dropdown
    - Prevents past-date entries
    - Uses Bootstrap-styled widgets via crispy_forms
  - FeedbackForm:
    - Simple textarea for submitting user comments

- views.py (Business Logic)
  - Handles:
    - Homepage (via PostList)
    - Feedback submission (about_me)
    - Contact page (contact_us)
    - Reservation creation, update, deletion, and listing
  - Key Features:
    - Uses @login_required to restrict sensitive views
    - Enforces model-level validation
    - Uses Django's messages framework for user feedback (success/error)

- urls.py (Routing)
  - Maps human-readable URLs to corresponding view functions
  - Enables paths like /about/, /reservation/form/, and /reservation/list/ to function properly

- settings.py
  - Registers all apps (e.g., reservation_app, about_app, crispy_forms)
  - Loads environment variables via env.py (e.g., Neon DB, secret key)
  - Manages static/template settings for Heroku or local development
  - Configures CSRF trusted domains and login/logout redirects

## Features to implement later

- Use API to implement google map with markers
- Implement through API Integration an external email system like sendemail to receive guest feedback.
- Menu Page - A page to display ***dish of the week*** and ***"what's special"***.
- Forgot/Reset password functionality

## Tools and Technology.

- Backend Framework
  - Django – Python web framework used for building views, models, authentication, and routing
- Python Packages
  - dj-database-url – Parses database URLs (used for Postgres)
  - python-dotenv – Loads environment variables from .env/env.py for secure configuration
  - psycopg2 / psycopg2-binary – PostgreSQL database adapter for Django
  - Gunicorn - A Python WSGI HTTP server compatible with Django and used to run the project on Heroku
  - whitenoise – Serves static files in production 
  - django-crispy-forms – Renders Bootstrap-styled Django forms more cleanly
  - crispy-bootstrap5 – Bootstrap 5 theme support for crispy-forms
  - django-allauth – Handles user registration, login, logout, and account management
- Frontend
  - Bootstrap 4.6 – For responsive design, layout, and UI components
  - HTML5 + CSS3 – Used in custom templates
  - Font Awesome – For icons and visuals
  - Google Fonts - Roboto , sans-serif
  - Colors used for styling:  #042a49, white, black,  brown, blue, #f05f40, #042a49
- Database
  - PostgreSQL – Relational database used via Neon DB as a cloud provider
  - Managed using Django ORM and models.py
- Hosting & Deployment
  - Heroku – Platform-as-a-Service (PaaS) used for deploying the Django application
  - Code Institute IDE / Gitpod – Cloud-based development environments used during build/testing
- Authentication
  - Django's built-in @login_required decorators – Used to protect views and ensure secure access
  - Allauth – Provides login, signup, logout, email handling 
- Mapping & Location
  - Google Maps iframe – Embedded map to display restaurant location (Abu Dhabi)
- Dev Tools
  - VS Code – Recommended IDE for Django development
  - GitHub  – For repository hosting and collaboration
  - Linters - https://pep8ci.herokuapp.com/# 
  - Broswer - Google Chrome

## Test and Validate - Functions

- The following functions were tested and validated
  - The Sign-up function 
  - The sign-in function 
  - The view and update reservation function 
  - The Delete reservation function
- No automated testing was done . All manual testing was done and screenshots attached

### Test and Validate Sign-up function.

- The sign-up form can be reached from two areas. 
  - when the user clicks on the "reserve now" button on the home page
  - from the sign-up page on the navbar.
- The sign-up form has validation checks for usernames and passwords.  

![reserve_now_modal](readme.doc/reserve_now_modal.png)

![sign_up_page](readme.doc/sign_up_page.png)

![username_valiadtion_signup](readme.doc/username_valiadtion_signup.png)

![password_validation_signup](readme.doc/password_validation_signup.png)

### Test and Validate Sign-in function

- The sign-in form can be reached from two areas. 
  - when the user clicks on the "reserve now" button on the home page
  - from the sign-up page on the navbar.
- The sign-in form has validation checks for usernames and passwords.  

![reserve_now_modal](readme.doc/reserve_now_modal.png)

![sign_in_page](readme.doc/sign_in_page.png)

![sign_in_validation](readme.doc/sign_in_validation.png)



### Test and Validate reservation-form function

- Once a user signs-up or signs-in, they are redirected to the rservation form.
- Users can book a table with their name, email, date, time, guest count, and a message.
- Form validations ensure:
  - No past dates allowed
  - Guest count must be between 1 and 10
- Reservations are saved to the database and associated with the logged-in user if authenticated.

![reservation_form](readme.doc/reservation_form.png)

![reservation_email_must](readme.doc/reservation_email_must.png)

![reservation_message_must](readme.doc/reservation_message_must.png)

![reservation_date_validation](readme.doc/reservation_date_validation.png)

![reservation_timeslot_validation](readme.doc/reservation_timeslot_validation.png)

![reservation_guest_validation](readme.doc/reservation_guest_validation.png)

![reservation_guest_exceed_validation](readme.doc/reservation_guest_exceed_validation.png)

- Once the signed in user submits the reservation, they are directed to the reservation list as show below.
- The guest can see only reservations made under the username they are logged in
- The guest can make mulitple reservations under different names and email addresses.
- The status shows "requested" as the admin is yet to confirm the booking.

![reservation_list_success.png](readme.doc/reservation_list_success.png)


### Test and Validate view/update-form function

- The screenshot below show the view for the logged in guest.
- The guest can see only reservations made under the username they are logged in
- The guest can make mulitple rservations under different names and email addresses.
- The status shows "requested" as the admin is yet to confirm the booking.

![reservation_list_success.png](readme.doc/reservation_list_success.png)


- As can be seen from the screenshot, the logged in user can update mulitple fields from the previous reservation.

![post_update.png](readme.doc/post_update.png)

# Deployment.

## Staticfiles

- All static files were consolidated under a single folder to allow to be accessed by the Heroku App

![static_files](readme.doc/static_files.png)

## Project Links - Github & Heroku

- Github Repository : https://github.com/Bobrac3023/Project4_roshan.git
  
- Heroku app : https://roshanproject4-8e7fe177e877.herokuapp.com/

## Deployment from GitHub

-The site was deployed to GitHub pages as below.  
  -In the GitHub repository
    - Navigate to the Settings tab
    - Select pages
    - select ***"Deploy from branch"***
    - Under ***Branch*** dropdown, change to ***Main*** from ***none***
    - From the ***Actions*** tab, select ***Deployment*** to check deployment status



## Wireframes

Wireframes were first sketched with pen and drawn using Microsoft Powerpoint 

Two custom models have been implemented in this project.


## Test and Validate - Code

-Code and functions were tested and validated using the three tools listed below:-  

- gitpod IDE environment    https://bobrac3023-project4rosh-u31s29dj3zv.ws.codeinstitute-ide.net/
- Python Linter - https://pep8ci.herokuapp.com

## User Stories and Methodology

GitHub Issues was used to plan and implement the user stories and test acceptance criteria
Link to github issues  :  

Each User Story contains **Acceptance Criteria -AC** to meet the  **Minimum Viable Product(MVP)** criterai for this project.
The user story acceptance criteria was based on ***As a, I can, So that*** or ***I Know I am done when***

The **MoSCoW Method of Prioritisation**(https://www.agilebusiness.org/dsdm-project-framework/moscow-prioririsation.html) was also refered to for the user story concepts based on **Must Have**, **Should Have** ,**Could Have** ,**Won’t Have**.


### Github Issues User story screenshot 

-Create new issue
![create_new_issue_1.png](readme.doc/create_new_issue_1.png)
-View of user stories on github issue
![user_story_view_github.png](readme.doc/user_story_view_github.png)
-View of Milestones for the project
![milestones.png](readme.doc/milestones.png) 
- View of user stories to milestones 
![user_story_view_github.png](readme.doc/user_story_milestone_assignment.png)

## Admin/Business Owner User Story and Acceptance Criteria 

No automated testing was done . All manual testing was done and screenshots attached 

The Admin Account Managment Milestone was created with two user stories and both were tracked in Github issues 
![admin_account_mgmt_milestone_2.png](readme.doc/admin_account_mgmt_milestone_2.png)
![admin_act_mgmt_milestone_complete.png](readme.doc/admin_act_mgmt_milestone_complete.png)

### As an admin, I want to create, update, and delete reservations so that I can assist users with their bookings. 
![approve_reservation.png](readme.doc/approve_reservation.png)

### As an admin, I want to view a list of all reservations so that I can manage booking schedules.###
![admin_panel](readme.doc/admin_panel.png)


## Guest Account Managment 

No automated testing was done . All manual testing was done and screenshots attached 

The Guest Account  Managment Milestone was created with two user stories and both were tracked in Github issues 
As a guest I should be able to sign-up to the restaurant portal with a unique username and password. 
As an guest, I should be able to login in to the restaurant portal based on my previous sign-up
![username_passwd_already_exists](readme.doc/username_passwd_already_exists.png)
![wrong_username_password.png](readme.doc/wrong_username_password.png)

## Guest Reservation Managment  

No automated testing was done . All manual testing was done and screenshots attached 

The Guest Reservation Managment Milestone was created with three user stories and tracked in Github issues 

### As a guest I should be able to login in and create a reservation. 

As a guest, I should be able to login in to update my reservation.
As a guest, I should be able to login in to cancel my reservation.

  





### Test and Validate CSS file ###
- Link https://jigsaw.w3.org/css-validator/validator

![style_css_validated](readme.doc/style_css_validated.png)

### Code insititute IDE output ###

![code_ide.png](readme.doc/code_ide.png)

### Python File validation ###

-Settings.py A note of caution here to the reader of this file. In the code-institue linter the lines which are flagged of as too long, when corrected produce an error when we run python3 manage.py runserver 

Screenshot show the out put of the linter after the changes were carried out. A few need to be changed in the ide setup. 

![setting_py.png](readme.doc/settings_py_linter.png)


![manage_py_linter.png](readme.doc/manage_py_linter.png)
![models_py_linter.png](readme.doc/models_py_linter.png)
![forms_py_linter.png](readme.doc/forms_py_linter.png)
![urls_py_linter.png](readme.doc/urls_py_linter.png)

