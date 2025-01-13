
## PROJECT4_ROSHAN - The Soul of India

## Introduction-Purpose of the Project
This project is based on a popular western India Maharashtrian hotel named Mai's Kitchen which traditionally serves authenticic and mouth watering cusine. The name **MAI** means **mother** in ***Marathi*** language.
The client can reserve a table online at a date and time of their choice and based on circumstances can change or delete the reservations.
The website is responsive, based on agile methodology and uses frontend development tools and technologies to provide a good UI/UX experience. 

## Features

- The project code is written in fron end development tools- HtML, CSS, Bootstrap,Django framework inside the code institute IDE.   
- Github is used to host the repository.  
- Heroku the dynamic websites platform is used to host backend language python.  
- PEP8 style guide was referenced to style the code
- The website offers simplicity and consistency within its structure.  Its structure was designed to be responsive on screens from 320px up to 2560px.
- The website is designed using the **"Mobile First"** Responsive approach using a structured layout and "meta" tags.
- The website has three pages including the landing page.  **"Home", "Register", "Login"**.
- The header includes the title of the website **" Taj Mahal- An Eternal Calling** and is common across all pages     
- The footer includes the **"copyright"** and **"social media icons"** and **link to download the menu**.  
- The chocie of foreground and background colors have the right contrast providing a rich user experience .  
- External links open in a seperate tab **social media"** and **link to download the menu** in the footer. 
- CSS media queries are used where appropriate for different screen sizes.  
- Relative paths are used for refering to folders and files.  
- **"Hover"** property used to hightlight pages on navigation bar, and social media icons in the footer.
- Bootstrap framework based on version 4.6.x https://getbootstrap.com/docs/4.6/getting-started/introduction/ is used extenstively. 
- Aria accessibility for screen readers.   

## Font family and colors.
- Google fonts used for styling. Download link:
  "https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,100;0,300;0,400;0,500;0,700;0,900;1,100;1,300;1,400;1,500;1,700;1,900&display=swap"
- Font-family used for styling : **Roboto**, **sans-serif**
- Colors used for styling:  #042a49, white, black,  brown, blue, #f05f40, #042a49
        
## Technology used in development and testing.

- **Google Chrome** as the Browser.
- Cloud-based platform **gitpod.io** and **github** used for designing and hosting the website.
- Bootstrap Framework v4.6.x- https://getbootstrap.com/docs/4.6/getting-started/introduction/
- Heroku - Heroku is a cloud platform that lets companies build, deliver, monitor and scale apps — we're the fastest way to go from idea to URL, bypassing all those infrastructure headaches. https://dashboard.heroku.com/apps/roshanproject4
- Devices with different viewports for testing the responsiveness - **Galaxy A54, iPhone 14 Pro, Galaxy A25, Asus AMD Ryzen7 4800H with 
  Radeon Graphics**.
- Django Framework based on Python 3.12.2.
- Linters - https://pep8ci.herokuapp.com/# 

### Libraries & Frameworks

- Django Framework based on Python 3.12.2.(https://www.djangoproject.com/) - Free and open source Python Web Framework
- Gunicorn (https://gunicorn.org/) - A Python WSGI HTTP server compatible with Django and used to run the project on Heroku
- PostgreSQL 0.5.x (https://www.postgresql.org/) - A powerful, open-source object-relational database system
- Pyscopg2 2.9.5 (https://www.psycopg.org/docs/) - A PostgreSQL database adapter for Python
- Heroku (https://www.heroku.com) - A cloud platform as a service
- Django Allauth (https://django-allauth.readthedocs.io/en/latest/) - Integrated set of Django applications addressing authentication and registration
- Bootstrap 4.6.2 (https://getbootstrap.com/docs/4.6/getting-started/introduction/) - A Framework for building responsive, mobile-fist sites
- whitenoise==5.3.0 (https://whitenoise.readthedocs.io/en/latest/) - WhiteNoise is used for serving static files in a Django application.
- sqlparse==0.5.0(https://pypi.org/project/sqlparse/) - SQLParse is a library used for parsing SQL queries in Python.


## Website Structure and feature description 
- The Django Design Philosopies are widely implmented to acheive the fundamental goals of **Loose Coupling, Less Code, Quick Development and Don't Repeat yourself (DRY), Explicit is better than Implicit and Consistency**.https://docs.djangoproject.com/en/4.2/misc/design-philosophies/
- The Structure is defined accordingly. The **Base.HTML** includes the **Head, Navbar** and **Footer** Sections.
- The **Home page** or **Index.HTML** includes the content - **Callout, Customer Reviews and Highlights**.
- The **login page** allows the guest to **login** to the **SQLite database** to reserve a table and **change** or **cancel** a reservation
- The **Register** page allows the guest to **sign up** at the restaurant website.
- Bootstrap framework based on version 4.6.x https://getbootstrap.com/docs/4.6/getting-started/introduction/ is used extenstively. 


## Website pages and feature description

### BASE.HTML 

### Head Section 
- The head section is based in the BASE.HTML file based on Django Design philosophies loose coupling philosophy
- The head section has the title **Soul of India**.
- The links to **google fonts, fontawesome, bootstrap, hover.css**, are all defined here.
- The styles.css file is also linked here.
- Viewport tag to respond to different resolutions, particularly mobile ones.

### Navbar Section
- Based on Django design philosophies, the "Navbar" section configued in Base.HTML includes the following.
- The Brand **MAI'S KITCHEN**.
- The **unordered list** for the header links inlcuding configuration to collapse into a **three bar icon** on small screens.
- The text**The way to your soul is through the stomach** prominently displayed on the right hand side of the header.


### Footer 
- The Footer displays "social media links" which open in a separate tab for ease of use.
- The Copy right section with the author's name is also prominently displayed on the left had section.
- The central part of the footer is reserved for guests to download the Menu. This menu is a PDF file and opens in a new tab so that the user does not have to navigate back to the page he was on.
- The PDF file is stored under the **project4_reservation** app section under the **static/css/menucard folder**.
- The Menu includes our restaurant address. 
- All social media links are "hover enabled" and open in seperate tabs.
- The following social media links have been configured- **Facebook, Twitter, Linkedin, Instagram, and Youtube**. 
- **A note of caution here** - MAI's Kitchen website does have a presence on any of the social media links, these links have only been configured to demonstrate front end design capability for this project.  


### INDEX.HTML 

 ### Callout Section 
 #### Screenshot of main landing page
![main_landing_page_codeide.png](readme.doc/main_landing_page_codeide.png)
![main_landing_page_heroku.png](readme.doc/main_landing_page_heroku.png)

- The **Callout section** includes a **Callout Jumbotron**.
- This jumbotron prominently displays the header **Authentic Maharashtrian Restaurant**
- **Jumbotron** also includes Bootstrap defined ARIA enabled butons for guests to make **reservations**, **update reservations** and **cancel reservations**.
- The **reservations button** is linked to a **form** configured in the **Modal section** 
- The update and cancel reservations button direct to the respective forms configured on **update_reservation.html** and **confirm_delete.html**

### Customer Reviews Section.

- As MAI's Kitchen is a new restaurant it is importnat that we highlight our acheivements and menu items.
- This section has reviews from a prominet food blogegr and a Bollyhood actor
- A future feature is to inlcude a section for guests to leave us with their reviews direcly through our website. 
  
### Highlighhts Section. 
- This section is used to highlight to MAI KITCHEN's patron on the uniqueness of the restaurant. 
- This is broken down into **Three Themes**
- ***Nourish the Soul*** - Mai’s Kitchen takes pride in serving traditional Maharashtrian cuisine, hailing from the western state of Maharashtra in India. 
- ***Made with Love*** -All our meals are made with love. We ensure ,flavours of the past continue to shape our future.
- ***Authentic and Vibrant*** - We aim to bring in seasonal menus, chef’s favourites, and special offers. 


## User Stories and Methodology

GitHub Issues was used to plan and implement the user stories and test acceptance criteria
Link to github issues  :  

Each User Story contains **Acceptance Criteria -AC** to meet the  **Minimum Viable Product(MVP)** criterai for this project.

The **MoSCoW Method of Prioritisation**(https://www.agilebusiness.org/dsdm-project-framework/moscow-prioririsation.html) was also refered to to under the usr staory concepts.
Each user story was classifyied based on **Must Have**, **Should Have** ,**Could Have** ,**Won’t Have**.


## Links to Github, Gitpod and Heroku

- External Link  
  
- Github issues : https://github.com/users/Bobrac3023/projects/2/views/1

- Heroku app :  https://roshanproject4-8e7fe177e877.herokuapp.com/
  
- Link to Github repository : https://bobrac3023-project4rosh-u31s29dj3zv.ws.codeinstitute-ide.net/

- Link to Gitpod workspace.  
  

## Features to implement later

- Use API to implement a google map with markers
- Implement an external email system like sendemail to receive guest feedback. This will be integrated using API.
- Menu Page - A page to display dish of the wekk and "what's special".  
* Forgot/Reset password functionality


## Deployment

### Deployment from GitHub
-The site was deployed to GitHub pages as below.  
-In the GitHub repository,
-   Navigate to the Settings tab,
-   Select pages
-   Under **Branch** dropdown, change to **Main** hub from **none**.

-select_branch_github_deployment

-From the **Actions** tab, select **Deployment** to check deployment status and capture external link.

## Testing and code validation

-Code and functions were tested and validated using the three tools listed below:-  

- gitpod IDE environment    https://bobrac3023-project4rosh-u31s29dj3zv.ws.codeinstitute-ide.net/
- Python Linter - https://pep8ci.herokuapp.com/# 


### Test,validate HTML Files

### Base.html
![]()

### Index.html

![]()

### Test and Validate CSS file ###
- Link https://jigsaw.w3.org/css-validator/validator

![style_css_validated](readme.doc/style_css_validated.png)


### Code insititute IDE output ###

![]()

### Python File validation ###

![]()


## Credits

- **Extra help to understand key concepts.**  

### Content creation assistance- reference code



## Table of Contents
* [Overview](#overview)
* [Agile Methodology](#agile-methodology)
* [User Experience (UX)](#user-experience-ux)
    * [Strategy / Site Goals](#strategy--site-goals)
    * [Scope / User Stories](#scope--user-stories)
    * [Structure / Design Choices](#structure--design-choices)
    * [Skeleton / Wireframes](#skeleton--wireframes)
    * [Surface](#surface)
* [Features](#features)
    * [Existing Features](#existing-features)
    * [Future Features](#future-features)
* [Technologies Used](#technologies-used)
* [Testing](#testing)
* [Bugs](#bugs)
* [Deployment](#deployment)
    * [Forking the GitHub Repository](#forking-the-github-repository)
    * [Creating a Local Clone](#creating-a-local-clone)
* [Credits](#credits)
* [Acknowledgements](#acknowledgements)

[Back To Top](#INDIAN-CURRY)


____


<details>
<summary>Instance of Kanban Board, screenshots of Epics and User Story</summary>
Kanban Board at this Iteration

![Kanband: Kanban board](documentation/kanbanboard.png)

![Kanband: userstories and epic board](documentation/userstories-epic.png)

</details>

____

## User Experience (UX)

### Strategy / Site Goals

Indian Curry restaurant aims to satisfy all the customers by maintaining an updated and user-friendly website with an online menu, reservation system, and contact information with map. It displays the story of the restaurant founder, as well as the attractive reasons for visiting Indian curry.

____

### Scope / User Stories

This section aims to determine what a user would expect from interacting with the website. Each User Story was recorded in [GitHub Issues](https://github.com/Pramilashanmugam/Restaurant/issues).  Scenarios of actions each type of user, including the business owner, wishes to take are listed below. Developer User Stories were also added to this section.

**As a Admin/Business Owner**

* As an admin, I want to add, update, and delete tables in the system so that I can maintain accurate table information. [#8](https://github.com/Pramilashanmugam/Restaurant/issues/8)

* As an admin, I want to create, update, and delete reservations so that I can assist users with their bookings. [#10](https://github.com/Pramilashanmugam/Restaurant/issues/10)

* As an admin, I want to view a list of all reservations so that I can manage booking schedules. [#9](https://github.com/Pramilashanmugam/Restaurant/issues/9)

* As a admin/Business owner I can accept online reservations only from next day and not from current day so that i can manage the reservation efficiently. [#16](https://github.com/Pramilashanmugam/Restaurant/issues/16)


**As a User**

* As a new user, I want to register an account so that I can access the reservation system. [#1](https://github.com/Pramilashanmugam/Restaurant/issues/1)

* As a registered user, I want to log in to my account so that I can manage my reservations. [#2](https://github.com/Pramilashanmugam/Restaurant/issues/2)

* As a user, I want to view a list of available tables so that I can see my options for making a reservation. [#4](https://github.com/Pramilashanmugam/Restaurant/issues/4)

* As a logged-in user, I want to make a reservation for a table on a specific date and time so that I can dine at the restaurant. [#5](https://github.com/Pramilashanmugam/Restaurant/issues/5)

* As a logged-in user, I want to view a list of my current and past reservations so that I can keep track of them. [#6](https://github.com/Pramilashanmugam/Restaurant/issues/6)

* As a logged-in user, I want to cancel an upcoming reservation so that I can change my plans if needed. [#7](https://github.com/Pramilashanmugam/Restaurant/issues/7)

* As a user, I want to receive a confirmation message after making a reservation so that I know it has been successfully booked. [#11](https://github.com/Pramilashanmugam/Restaurant/issues/11)

* As a user, I want to receive a confirmation message after canceling a reservation so that I know it has been successfully canceled. [#12](https://github.com/Pramilashanmugam/Restaurant/issues/12)

* As a user, I want the reservation system to be accessible on different devices (desktop, tablet, mobile) so that I can make and manage reservations conveniently. [#13](https://github.com/Pramilashanmugam/Restaurant/issues/13)

* As a user, I want to see clear error messages if something goes wrong (e.g., trying to book a table that is already reserved) so that I understand what the issue is and how to resolve it. [#15](https://github.com/Pramilashanmugam/Restaurant/issues/15)

* As a user, As a user I should not be allowed to book a slot on past time so that the booking can be always a valid booking.. [#17](https://github.com/Pramilashanmugam/Restaurant/issues/17)

The following User Stories were added features to the website which was not included in the initial kanban board as these features were developed during the development stage which make the website run more smoothly and give the users a better experience using the website. 

**As a Developer**

* I can add a favicon to the tab with website's title so that it gives users more visual feedback when looking at their tabs on their browser.

* I can display success and error messages upon form submission so that the user has a better experience with the site.

* I can restrict access on users' reservation so that only the logged in user and admin are able to access, update and delete said user's reservation.

* I can place validations on the datefield so that users are not allowed to pick dates in the past and dates/times that have already been booked.

* I can place validations on the seats so that users are not allowed to enter number of guest above the table capacity.

* I can restrict user to enter a maximum of 1000 characters in the note field.

* I can restrict the entry in name field as only alphabets.

___

### Structure / Design Choices

The website offers simplicity and consistency within its structure.  Its structure was designed to be responsive on screens from 320px up to 2560px.

The Navigation menu displays the Indian Curry logo and a Hamburger button (on mobile) with links to the Home, Menu, Register, Login and Logout pages, for easy navigation. The Navigation menu is repeated across all pages.

The Footer displays social media links which open in a separate tab for ease of use. It also displays the Restaurant's address and contact informations, including map, phone and email links which open in a separate tab. The footer is also repeated across all pages to keep the design uniform and for ease of access.

The Home Page clearly delineates the purpose of the site with 3 large Hero which consists of the name of the business, a slogan and buttons to navigate to menu and table booking.  Other informations like story is included.

The Menu Page gives a more detailed description of the various food items in different categories, like Starter, Main course, Kids menu, Beverage and Desserts. It also provides the link to book a table and view already reserved tables.

The Registeration & Authentication Pages, also accessed through the Navigation Menu, welcome the users to the service and are simple, clear and conform with the standards used across the web.

The Make a Reservation and My booking history pages, are accessed only for registered user to book, update, delete his/her table reservations.

<details>

<summary>The Database Schema used for this project</summary>

![Entity Relationship Diagram](documentation/erd.png)

Two custom models have been implemented in this project.

* **The Table Model** - Table to Reservation has One-to-Many (A table can have multiple reservations over time):

    - id (PK)
    - table_number
    - seating_capacity

* **The Reservation Model** - User to Reservation: One-to-Many (A user can make multiple reservations):

    - id (PK)
    - user_id (FK)
    - table_id (FK)
    - name
    - date
    - time
    - guests
    - phone
    - notes

</details>


___

### Skeleton / Wireframes

Wireframes were first sketched with pen and paper. This method helped me with brainstorming, deciding the most essential parts for the website and getting a feel for the website as a whole. They were then wireframed in [Balsamiq](https://balsamiq.com/wireframes/) to give a closer indication of the design.  Through the design phase some elements were changed to allow for a better user experience.

<details>

<summary>Balsamiq Wireframes</summary>

**Home Page**

![Home mobile](documentation/homepage-wiremob.png)

![Home desktop](documentation/homepage-wiredesktop.png)

**Menu Page**

![Menu mobile](documentation/menu-wiremob.png)

![Menu desktop](documentation/menupage-wiredesktop.png)

**Make a Reservation**

![Make a reservation mobile](documentation/makeareservation-mob.png)

![Make a reservation desktop](documentation/makeareservation-desktop.png)

**My Booking History**

![My Booking History mobile](documentation/viewbooking-wiremob.png)

![My Booking History desktop](documentation/viewbooking-wiredesktop.png)

**Cancel Confirmation**

![Cancel Confirmation mobile](documentation/cancelconfimation-mob.png)

![Cancel Confirmation desktop](documentation/cancelconfirmation-desktop.png)

**Update a Reservation**

![Update a reservation mobile](documentation/makeareservation-mob.png)

![Update a reservation desktop](documentation/makeareservation-desktop.png)

**Signup**

![Signup mobile](documentation/signup-wiremob.png)

![Signup desktop](documentation/signup-wiredesktop.png)

**Signin**

![Signin mobile](documentation/signin-wiremob.png)

![Signin desktop](documentation/signin-wiredesktop.png)

**SignOut**

![SignOut mobile](documentation/signout-wiremob.png)

![SignOut desktop](documentation/signout-wiredesktop.png)

</details>

___

### Surface

This section defines the visual language of the website.

* Colour Scheme

Mostly White and Black colour palette was chosen for this website text and background. The logo has a wine colour palette. The other colourful colours like red, green, yellow was used on buttons.

![White and Black colour palette](documentation/colorpalette.png)

* Typography

Arial and sans-serif fonts were used throughout the website.

* Icons

[uxwing](https://uxwing.com/) social media, map, phone and email icons were used for the Footer.  They are used as interactive links and have an aria-label which gives the relevant information to screen readers to read out to the users.

[Back To Top](#table-of-contents)

____

## Features

### Existing Features

**Header & Navigation**

Featured on all pages, the fully responsive header includes:

* A link on the Logo which brings the user to the home page.
* A hamburger button on mobile which opens up a navigation list with links to the Home, Menu, Register and Login pages. This helps reduce the clutter on the header by keeping the page links neatly stowed away until the user navigates to the hamburger button.
* Links to the Home, Menu, Register and Login pages on tablet and desktop which help the user to navigate easily from page to page, without having to revert back to the previous page via the back button. 
* The last two links change depending on the user's status. If the user is not logged, in the Register and Login links are displayed, while the Profile and Logout links are displayed if the user is logged in.

<details>

<summary>Click to view screenshots of Navigation features</summary>

        Navigation closed on mobile  
![Header on mobile closed](documentation/navigationclosed-mob.png)

        Navigation open on mobile
![Header on mobile open](documentation/navmobview.png)

        Navigation open for logged user mobile
![Header on mobile logged user](documentation/navloggedin-mob.png)

        Navigation on tablets & desktops
![Header on tablet](documentation/navloggedout.png)

        Navigation for logged user on tablets & desktops
![Header on tablet logged user](documentation/navloggedin-desk.png)

</details>

<br>

**Footer**

Featured on all pages, the responsive footer is valuable to the users as it encourages them to get in touch via phone or email if they prefer that method of contact and it also allows the users to keep connected via social media. It includes:
* The business's address and a map location is given to reach us.
* Contact details are links which direct the user to the relevant apps. On mobile, the telephone number when clicked will bring up a call feature, while the email address will open up an email app on tablet or desktop as well.
* Social links open in a new tab so that users are not directed away from the website. 
* A Simple Copyright disclaimer shown at the bottom of the footer.
* All links have a pointer cursor to help users identify them as links.

<details>

<summary>Click to view screenshots of Footer features</summary>

        Footer on mobile 
![Footer on mobile](documentation/mobfooter.png)

        Footer on tablet/desktop 
![Footer on tablet/desktop](documentation/desktopfooter.png)

</details>

<br>

**Landing Page**

The Home page hero on the Landing page takes up more than half the viewport of any screen size. It includes a carousel with three images of indian dishes, spices and the restaurant interiors. A slogan which captures the essence of indian food is included on each image.  It also acts a Call to Action(CTA) as it includes two buttons inviting the user to book a Table and view the Menu.  The button has a hover and focus effect as demonstrated below. 

<details>

<summary>Click to view screenshots Landing page features</summary>

        Landing page on mobile
![Landing page on mobile](documentation/hero-mob.png)

        Landing page on tablet/desktop
![Landing page on tablet/desktop](documentation/hero-desktop.png)

</details>

<br>

**Menu Page**

The responsive Menu page is reachable via the Menu link in the navigation bar as well by clicking the 
"Our Menu" button on all three images on the carousel on Home page. It includes the following:
* More detailed information on the restaurant opening timing for Lunch and Dinner.
* The Menu is very well categorised as Appetizers, Main Course, Indian Breads, Desserts, Beverages and Kids Menu, which enhances the customer experience.
* The background and text are very well styled for a better visual experience.

<details>

<summary>Click to view screenshots of the Menu page</summary>

        Menu page on mobile
![Menu page on mobile](documentation/menucontent-mob.png)

        Menu page on tablet/Desktop
![Menu page on tablet/desktop](documentation/menucontent-desktop.png)

</details>

<br>

**Register**

The website has the functionality for a user to register for an account.  
* The fully responsive registration form can be accessed through the navigation bar or when user click on sign up link in Sign in page.  
* At the top it also has a link to the Login form for users who have already registered for an account. The cursor changes to pointer when lands on signup. 
* It uses django-allauth to provide all the settings for user authentication and includes the fields below.  The form was extended to also include fields for first and last name.

    - Username (unique)
    - Email (optional)
    - Password
    - Password repeat

* The Register page's styles are consistent with the rest of the website.  The form is submitted via the Signup button at the bottom of the form. This button provides good contrast against the white background of the form and has a hover effect when cursor lands on the button.
* When the users click on the Signup button they are directed to the Home page, on navbar you will see only logout replacing register and login links.

<details>

<summary>Click to view screenshots</summary>

![Register Form on mob](documentation/signup-mob.png)

![Register Form on Tablet/Desktop](documentation/signup-desktop.png)

</details>

<br>

**Login**

A register user can access the login form through the navigation bar or also when clicked on book a table button on Home and menu pages, view my booking button on menu page user will be redirected to signin page if not already logged in.  
* It includes a small welcome message and a link to the Sign up form for users who have not yet registered for an account.
* It uses django-allauth to provide all the settings for user authentication and includes the following fields:  

    - Username
    - Password

* The responsive Login page is styled in a consistent manner with the rest of the website.  The form is submitted via the sign in button at the bottom of the form. This button provides good contrast against the white background of the form and has a hover effect when mouse lands on the button.
* When users click on the Login button they are directed to the home page.
* A message for successful login shown on Navbar.

<details>

<summary>Click to view screenshots</summary>

![Login Form on Mob](documentation/signin-mob.png)

![Login Form on Tablet/Desktop](documentation/signin-desktop.png)

![success message on Tablet/Desktop](documentation/login-success-msg.png)

</details>

<br>

**Logout**

The website has functionality for a logged in user to log out.
* The Logout form can only be accessed from the navigation bar and only when the user is logged in.
* It confirms with the logged in user that they want to log out.
* Its style is consistent with the rest of the webpage and it is fully responsive.
* The Sign Out button logs out the users and directs them back to the Home page.
* A message on successful logout shown on Navbar.

<details>

<summary>Click to view screenshots</summary>

![Logout option on navbar](documentation/logout-navbar.png)

![Logout reconfirmation](documentation/reconfirmation.png)

![success message on Tablet/Desktop](documentation/success-logout-msg.png)

</details>

<br>

**Make a Reservation**

The website gives the user the functionality to book/reserve a table via the book a table button on the Home and Menu pages.
* A user must be logged in to access the Make a reservation page.
* If a logged in user tries to book a table without filling in the reservation form, they will get a notice directing them to first fill in the form in the make a reservation page.  
* All the fields in the form are set as required field, hence any field left blank will not allow user to book a table until it is filled.
* The style is consistent with the rest of the webpage and it is fully responsive.
* The Table and Time fields are dropdown fields, from which the user can select a value.
* The Name Field accepts only alphabets and if any other character entered, a message asking user to enter only alphabets appears. 
* The Seat Field accepts only numbers > 0, negative numbers are not accepted.
* The Phone Field accepts only numbers, if invalid input received a error message will guide user to enter only number.
* The Date field only accepts current and future dates upto 6 months from the current date. Mondays are not accepted as restaurant is closed on mondays.
* The Time field lists the time slots according the restaurant open time and is also validated along with the Date field so that it doesn't accept double bookings.
* The Note Field can accept a maximum of 1000 character.
* If the information entered does not pass validation, the Submit button directs the user back to the form.  Error messages point out the fields not passed and an error alert is displayed on the bottom of each field. 
* If the information entered passes validation, the Submit button directs the user back to the My booking history page, where they can view their existing and new booking and a message shown on navbar on successful reservation
* Each booking will have corresponding edit/update and cancel button for the user to manipulate his booking.

<details>

<summary>Click to view screenshots</summary>

        When fields left empty, it notices a message with hovered on link
![Notice for blank field](documentation/blankfields.png)

        Booking a table with valid datas
![Fields with valid data](documentation/valid-datas.png)

        On Successful reservation, a message on navbar
![message on navbar](documentation/makereservation-success-message.png)

        TableSeat validation - seat number should not be more than the capacity of the table
![Table Seat capacity validation](documentation/tableseat.png)

        Error message on name field if non alphabet character enter
![Fields with valid data](documentation/nameinvalid.png)

        Datefield Validation - only monday
![Datefield restricted on monday](documentation/mondaydate.png)

        DateTime Validation - already booked
![DateTime error this slot is already booked](documentation/reservationexists.png)

        Seat Validation - number should not be 0 and negative
![Seat number cannot be 0 or negative](documentation/seatnumber.png)

        Phone Validation - only numbers are accepted
![Phone field accepts only numbers](documentation/phonefield.png)

        Notes Validation - should not exceed 1000 characters
![note field with max length 1000](documentation/notefield.png)

        Successful reservation- with valid datas, reservation confirmation
![Reservation confirmation](documentation/confimation.png)

</details>

<br>

**View Bookings**

The website gives the user the functionality to read more details about their appointments via the View my booking button on Menu page or after valid data entry received from make a reservation page it redirects to My booking history page.
* A user must be logged in to access the My booking history page.
* When the user clicks on the View my bookings button in the Menu page, only reservations done from the particular logged in users data will be displayed on page.
* This consists of a Make a reservation and Go back to Homepage buttons which directs the user back to respective pages. 
* Each reservation includes:
  - the Name, 
  - Number of guests
  - the Date & Time of reservation, 
  - The table number booked and the capacity of the table, 
  - an Update and a Cancel button.
* The information on the reservation changes if customer chose to update using update button and also when a reservation id deleted. View screenshots below for details. 
* The style is consistent with the rest of the webpage and it is fully responsive.  All buttons have focus and hover effects.
* A success message on updation and cancellation will appear on the navbar.

<details>

<summary>Click to view screenshots</summary>

        My booking history page
![My booking history](documentation/bookinghistory.png)

        When an existing reservation is updated
![After updation](documentation/updatedbooking.png)

![After updation success message](documentation/update-navbar-message.png)

        When a reservation is cancelled
![reservation cancellation](documentation/cancellationcofirm.png)

![After deletion success message](documentation/cancel-navbar-message.png)

</details>

<br>

**Admin Panel**

The website offers the business owner the functionality to view and interact with the database in the Django Admin panel.
* The panel is reachable by typing `/admin/` at the end of the website's URL in the URL bar.
* This brings the user to the Django Administration Login Page, where the user is asked for their Username and Password.  Only users with Superuser status has permission to login. 
* The Superuser has permissions to add, change, delete and view everything while the user with the status of staff has only certain permissions granted by the Superuser.
* The restaurant owner has been granted the Superuser status for now, in order to have full access of the Admin's Panel. 
* The registered Reservation and Table models can be viewed in the Admin Interface where tables for Reservations and Tables are listed under the relevant app names. Accounts and Authentication & Authorisation list tables with information gathered through registration. 
* The Superuser can add a Table and its capacity in the add table option
      
* Using the menu on the far right, the Superuser is also able to filter this reservation table by:

    - Date
    - Time
    - User
    - Table

* The Superuser can also use search option to filter the field he wants from the reservations table 

<details>

<summary>Click to view screenshots</summary>

        Reaching the Admin Panel
![URL to reach the Admin panel of the website](documentation/adminpanellink.png)

        Django Administration Login Page
![Django Admin login page](documentation/djangoadmin.png)

        Django Administration Interface
![Django Admin interface](documentation/djangointerface.png)

        Django Administration Interface for Reservation
![Full Admin interface with Reservation table](documentation/reservationtable.png)

        Django Administration Interface for Table
![Full Admin interface with Table Model](documentation/tablemodel.png)

</details>

<br>

[Back To Top](#table-of-contents)
____

### Future Features

* Validation on Time field - At the moment a user can select any time slot from the given drop down, a validation is considered here to allow user to pick time only from the current time and not in the past.
* Menu on Menu Page - This page will be revisited everytime when there is an addition or deletion of food item in the Restaurant.  
* Add a welcome message - A welcome message with user name on navbar is planned to implement for a better user experience, and this feature would be only for logged in. 
* Add a review Section - Customer review on restaurant to be implemented, which would help in improvements.
* Forgot/Reset password functionality
* Confirmation of reservation/reminder to user via texts or emails.
* A validation in booking history - The oldest booking which are no more valid against the current and future date needs to be removed from the booking history.

[Back To Top](#table-of-contents)

____

## Technologies Used




[Back To Top](#table-of-contents)

____

## Testing

All testing information can be found in [TESTING.md](TESTING.md).

[Back To Top](#table-of-contents)

____


### Bugs

Known bugs are resolved or an alternative solution been identified and fixed. However there could also be unknown bugs, which was not discovered during the rigorous testings.

<details>
<summary>First Deployment Bug</summary>

Problem: When the first deployment was tried on Heroku, An application error was encountered 

        Application error
![Application error](documentation/applicationerror.png)

Solution: This issue was shorted out by updating my Procfile with correct file name.
</details>
<details>
<summary>Bugs during Development</summary>

Problem: Tried to use sticky-top class on navbar but on midway it stops working on menu page on mobile.

Solution: Removed sticky-top class as suggested by my mentor.

Problem: Phone field was not accepting all combination of number, since it was an integer field. 

        Phone field error
![Phone field error](documentation/phonefieldbug.png)

Solution: This issue was shorted out by changing the phonefield to charField and also by recreating a new database file as there was problem in Deployment.


Problem: since the Phone field was changed from integer to string, there was database, session error. 

        Database error
![Database error](documentation/databaseerror.png)

Solution: This issue was shorted out by changing the database url as too many manipulation on previous database file was not allowing the changes in deployment. A new superuser was created to overcome this error as advised by Tutor.

</details>

<details>
<summary>Bugs encountered during Testing</summary>

**Make a reservation Form Fields**

Problem: Name field accepting all the characters including special chars and numbers

Solution: Validation included to accept only alphabets.
```
if not value.isalpha():
        raise ValidationError(
            'Name can only contain alphabetic characters. '
            'Please check your entry.'
        )
```


Problem: Date field accepting past date and all future dates

Solution: Validation included to accept only current date and future date upto 6 months.

```
today = timezone.now().date()
    # Approximation for 6 months
    six_months_from_today = today + datetime.timedelta(days=6*30)
    if not (today <= value <= six_months_from_today):
        raise ValidationError(
            "Reservation date must be between today and the next 6 months.")
```

Problem: Seat field accepting zero and negative numbers

Solution: Two diff validation included to accept only number from 1 till the capacity of the Table size.

```
if value <= 0:
        raise ValidationError(
            'The number of guests must be greater than zero. '
            'Please enter a valid number.'
        )

if table and guests:
            if guests > table.capacity:
                self.add_error('guests', f"The number of guests exceeds the "
                               f"table's capacity of {table.capacity}. "
                               f"Please choose another table.")
```


Problem: Note field accepting unlimited number characters.

Solution: Validation included to accept only characters upto 1000.

```
notes = forms.CharField(
        max_length=1000,
        widget=forms.Textarea(
            attrs={'class': 'form-control', 'maxlength': 1000}
        )
)
```

</details>

<details>
<summary>Bugs Remaining</summary>

### Bugs Remaining

**Make a reservation Form Fields**

    * Time field validation
    Problem: The Time field currently accepts the past time on current date this issue was identified during testing. Tried to fix this with a validation against the current time  however the fix was unsuccessful as the datatype for time was initially assigned as charfield. Hence this may required a complete revamp on model and may not be fixed in a short span of time. Hence came up with a temporary solution as given below and marked this issue in kanban board as bug and moved to backlogs for later action.

    Temporary Solution: Customer can avail online reservation not on the current day but from the next day. A new validation included in date field to accept the reservation after one day.

    ```
    date = self.cleaned_data.get('date')
        if date:
            if date.weekday() == 0:  # Monday is 0
                raise ValidationError('Sorry we are closed on Mondays. '
                                      'Please choose another day.')
            if date <= timezone.now().date() + timedelta(days=0):
                raise ValidationError('Online reservations can only be made'
                                      ' at least one day in advance. '
                                      'Please choose another date.')
        return date
    ```
</details>

<br>

[Back To Top](#table-of-contents)

____

## Deployment

For good practice, this project was deployed early to [Heroku](https://www.heroku.com) in order to save time and avoid nasty surprises later on.

After installing Django and the supporting libraries, the basic Django project was created and migrated to the database. 

The database provided by Django [db.sqlite3](https://docs.python.org/3/library/sqlite3.html) is only accessible within the workspace environment. In order for Heroku to be able to access the database, a new database suitable for production needs to be created.  Heroku offers a postgres add-on at an extra charge. I am using a postgreSQL database instance hosted on [CI Database](https://dbs.ci-dbs.net/) as this service is free. 

<details>
<summary>Steps taken before deploying the project to Heroku</summary>

### Create the Heroku App

1. Login to Heroku and click on the top right button ‘New’ on the dashboard. 
2. Click ‘Create new app’.
3. Give your app a unique name and select the region closest to you. 
4. Click on the ‘Create app’ button.

### Create the PostgreSQL Database

1. Login to https://dbs.ci-dbs.net/.
2. step 1: enter your email address and submit.  
3. step 2: creates a database.  
4. step 3: receive the database link on your email id. 

### Create the env.py file

With the database created, it now needs to be connected with the project.  Certain variables need to be kept private and should not be published to GitHub.  

1. In order to keep these variables hidden, it is important to create an env.py file and add it to .gitignore.  
2. At the top **import os** and set the DATABASE_URL variable using the `os.environ` method. Add the URL copied from instance created above to it, like so:
`os.environ[“DATABASE_URL”] = ”copiedURL”`
3. The Django application requires a SECRET_KEY to encrypt session cookies.  Set this variable to any string you like or generate a secret key on this [MiniWebTool](https://miniwebtool.com/django-secret-key-generator/).
`os.environ[“SECRET_KEY”] = ”longSecretString”`

### Modify settings.py 

It is important to make the Django project aware of the env.py file and to connect the workspace to the new database. 

1. Open up the settings.py file and add the following code. The if statement acts as a safety net for the application in case it is run without the env.py file.
```
import os
import dj_database_url

if os.path.isfile(‘env.py’):
    import env
```
2. Remove the insecure secret key provided by Django and reference the variable set in the env.py file earlier, like so:
```
SECRET_KEY = os.environ.get(‘SECRET_KEY’)
```
3. Hook up the database using the dj_database_url import added above.  The original DATABASES variable provided by Django connects the Django application to the created db.sqlite3 database within your repo.  This database is not suitable for production so comment out the existing db.sqlite3 and include the command as below for the new database. 

```
# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

# DATABASES = {
#   'default': {
#       'ENGINE': 'django.db.backends.sqlite3',
#       'NAME': BASE_DIR / 'db.sqlite3',
#   }
# }

DATABASES = {
    'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
}
```

**NOTE**: If at the start of the development you are using the local db.sqlite3, make sure to add it to the .gitignore file, so as not to make the mistake of pushing it to your repository.  

5. Save and migrate this database structure to the newly connected postgreSQL database.  Run the migrate command in your terminal
`python3 manage.py migrate`

### Connect the Database to Heroku

1. Open up the Heroku dashboard, select the project’s app and click on the ‘Settings’ tab.
2. Click on ‘Reveal Config Vars’ and add the DATABASE_URL with the value of the copied URL from the database instance created on CI database.
3. Also add the SECRET_KEY with the value of the secret key added to the env.py file. 
4. If using gitpod another key needs to be added in order for the deployment to succeed.  This is PORT with the value of 8000.

### Setup the Templates Directory

In settings.py, add the following under BASE_DIR 
`DIRS = os.path.join(BASE_DIR, "templates")`

### Add the Heroku Host Name

In settings.py scroll to ALLOWED_HOSTS and add the Heroku host name.  This should be the Heroku app name created earlier followed by `.herokuapp.com`.  Add in `’localhost’` so that it can be run locally.
```
ALLOWED_HOSTS = [‘heroku-app-name.herokuapp.com’, ‘localhost’]
```

### Create the Directories and the Process File

1. Create the media, static and templates directories at the top level next to the manage.py file. 
2. At the same level create a new file called ‘Procfile’ with a capital ‘P’.  This tells Heroku how to run this project.  
3. Add the following code, including the name of your project directory. 
```
web: gunicorn tailors_thimble.wsgi
```
* ‘web’ tells Heroku that this a process that should accept HTTP traffic.
* ‘gunicorn’ is the server used.
* ‘wsgi’, stands for web services gateway interface and is a standard that allows Python services to integrate with web servers.
4. Save everything and push to GitHub. 

</details>

<details>
<summary>First Deployment</summary>

### First Deployment

1. Go back to the Heroku dashboard and click on the ‘Deploy’ tab.  
2. For deployment method, select ‘GitHub’ and search for the project’s repository from the list. 
3. Select and then click on ‘Deploy Branch’.  
4. When the build log is complete it should say that the app has been successfully deployed.
5. Click on the ‘Open App’ button to view it and the Django “The install worked successfully!” page, should be displayed. 

</details>

<details>
<summary>Final Deployment</summary>

### Final Deployment

1. When development is complete, if you had left `DEBUG = True` in the settings.py file, make sure to change it to `False`. You don't have to change anything if you had used `DEBUG = 'DEVELOPMENT' in os.environ` as your env.py file is ignored by GitHub. 
2. Commit and push your code to your project's repository.
3. Then open up Heroku, navigate to your project's app. Click on the 'settings' tab, open up the config vars and delete the DISABLE_COLLECTSTATIC variable. 
4. Navigate to the 'Deploy' tab and scroll down to 'Deploy a GitHub branch'.
5. Select the branch you want to deploy and click on the 'Deploy branch' button. When the app is deployed, you should see a message in the built log saying "Your app was successfully deployed".  Click 'View' to see the deployed app in the browser. Alternatively, you can click on the 'Open App' button at the top of the page. 

</details>

_____

### Forking the GitHub Repository

<details>
<summary>Steps to Fork the GitHub Repository</summary>

Forking allows you to view and edit the code without affecting the original repository

1. Locate the GitHub repository. Link to this repository can be found [here](https://github.com/Pramilashanmugam/Restaurant).
2. Click on 'Fork', in the top right-hand corner.
3. This will take you to your own repository to a fork with the same name as the original branch.

</details>

_____

### Creating a Local Clone

<details>
<summary>Steps to Creating a Local Clone</summary>

1. Go to the GitHub repository. Link to this repository can be found [here](https://github.com/Pramilashanmugam/Restaurant).
2. Click on 'Code' to the right of the screen. This will open a dropdown. Click on HTTPs and copy the link.
3. Open Git Bash in your IDE and change the current working directory to the location where you want the cloned directory.
4. Type `git clone`, paste the URL you copied earlier, and press Enter to create your local clone.

More information on Creating and Managing repositories can be found [here](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)
<br>

</details>

[Back To Top](#table-of-contents)

____

## Credits

### Code

The following walkthroughs helped me get my project in shape.  I have adapted the code in these walkthroughs for the needs of my project.
* Code Institute's "I Think Therefore I Am Blog" which is found in the CI's LMS for the Diploma in Software Development.
* JVL code's [Python Django Tutorial: Full-Featured Web App](https://www.youtube.com/watch?v=g5vFWHajutg&t=6263s)
* Dee Mc's [Django Tutorial On How To Create A Recipe blog](https://tinyurl.com/mrx7jbjt) 
* Indian Pepper Website [Inspired some designing ideas like reservation form](https://www.indianpepper.de/)
* Readme model [Inspired from Tailors_thimbel-MoniPar](https://github.com/MoniPar/tailors_thimble) 

Pages I referred to a lot:

* [Django Documentation](https://docs.djangoproject.com/en/3.2/)
* [Bootstrap Documentation](https://getbootstrap.com/docs/4.6/getting-started/introduction/)
* [Django Allauth](https://django-allauth.readthedocs.io/en/latest/)
* [Google](https://www.google.de/)
* For Documentation [ChatGPT](https://chatgpt.com/)


Other pages, questions, fellow student's projects I found useful:

* Active Tag on Bootstrap with Django [Stackoverflow Question](https://stackoverflow.com/questions/32931436/active-tag-on-bootstrap-with-django)
* Change button active colour in Bootstrap [Bootstrap](https://getbootstrap.com/docs/4.0/components/buttons/)
* Validating Date from current date [Stackoverflow Question](https://tinyurl.com/47euefym)
* Validating Date to accept upto 6 months from current date [Stackoverflow Question](https://tinyurl.com/ke97u2ev)
* Slack community [Slack members](https://app.slack.com/)
* Student Project [Tailors_thimbel-MoniPar](https://github.com/MoniPar/tailors_thimble)
* Student Project [Flight reservation - Carl Murray](https://github.com/CarlMurray/flyUX-pp4)


### Media

* Indian Curry logo and favicon designed from [Adobe logo maker](https://www.adobe.com/in/express/create/logo)
* Home Page Hero Image in carousel[Anilsharma26 | Pexels](https://pixabay.com/photos/spices-biryani-indian-cuisine-7286740/)
* Home Page Hero Image in carousel[Anilsharma26 | Pexels](https://www.pexels.com/photo/indian-foods-on-a-surface-10580198/)
* Home Page Hero Image in carousel[cottonbro | Pexels](https://www.pexels.com/photo/an-empty-restaurant-9316203/)

* Background Image [Charlotte May | Pexels](https://www.pexels.com/photo/cup-of-masala-chai-on-table-5946623/)


[Back To Top](#table-of-contents)

____

## Acknowledgements

I would like to thank the following people who inspired, motivated, guided, helped and supported me along this Portfolio Project 4 journey.
* My mentor Rory Patrick for the guidance and the encouragement. 
* Patrick Hladun and the many people on Slack, for helping me out of a few messes I got into and for teaching me a few tricks along the way.
* Tutors namely Thomas, Rebecca, Alan, Roo who have been a great support during hard times.
* My father, whom i lost recently during the mid of PP4 project, as always been an inspiration to complete any task.
* My Husband, whose critics have always helped me to come back with a better solution.



![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

[Back To Top](#table-of-contents)
____


![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome Roshan Sequeira,

This is the Code Institute student template for Gitpod. We have preinstalled all of the tools you need to get started. It's perfectly ok to use this template as the basis for your project submissions.

You can safely delete this README.md file or change it for your own project. Please do read it at least once, though! It contains some important information about Gitpod and the extensions we use. Some of this information has been updated since the video content was created. The last update to this file was: **June 18, 2024**

## Gitpod Reminders

To run a frontend (HTML, CSS, Javascript only) application in Gitpod, in the terminal, type:

`python3 -m http.server`

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

To run a backend Python file, type `python3 app.py` if your Python file is named `app.py`, of course.

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

By Default, Gitpod gives you superuser security privileges. Therefore, you do not need to use the `sudo` (superuser do) command in the bash terminal in any of the lessons.

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to *Account Settings* in the menu under your avatar.
2. Scroll down to the *API Key* and click *Reveal*
3. Copy the key
4. In Gitpod, from the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you, so do not share it. If you accidentally make it public, you can create a new one with _Regenerate API Key_.

### Connecting your Mongo database

- **Connect to Mongo CLI on a IDE**
- navigate to your MongoDB Clusters Sandbox
- click **"Connect"** button
- select **"Connect with the MongoDB shell"**
- select **"I have the mongo shell installed"**
- choose **mongosh (2.0 or later)** for : **"Select your mongo shell version"**
- choose option: **"Run your connection string in your command line"**
- in the terminal, paste the copied code `mongo "mongodb+srv://<CLUSTER-NAME>.mongodb.net/<DBname>" --apiVersion 1 --username <USERNAME>`
  - replace all `<angle-bracket>` keys with your own data
- enter password _(will not echo **\*\*\*\*** on screen)_

------

## Release History

We continually tweak and adjust this template to help give you the best experience. Here is the version history:

**June 18, 2024,** Add Mongo back into template

**June 14, 2024,** Temporarily remove Mongo until the key issue is resolved

**May 28 2024:** Fix Mongo and Links installs

**April 26 2024:** Update node version to 16

**September 20 2023:** Update Python version to 3.9.17.

**September 1 2021:** Remove `PGHOSTADDR` environment variable.

**July 19 2021:** Remove `font_fix` script now that the terminal font issue is fixed.

**July 2 2021:** Remove extensions that are not available in Open VSX.

**June 30 2021:** Combined the P4 and P5 templates into one file, added the uptime script. See the FAQ at the end of this file.

**June 10 2021:** Added: `font_fix` script and alias to fix the Terminal font issue

**May 10 2021:** Added `heroku_config` script to allow Heroku API key to be stored as an environment variable.

**April 7 2021:** Upgraded the template for VS Code instead of Theia.

**October 21 2020:** Versions of the HTMLHint, Prettier, Bootstrap4 CDN and Auto Close extensions updated. The Python extension needs to stay the same version for now.

**October 08 2020:** Additional large Gitpod files (`core.mongo*` and `core.python*`) are now hidden in the Explorer, and have been added to the `.gitignore` by default.

**September 22 2020:** Gitpod occasionally creates large `core.Microsoft` files. These are now hidden in the Explorer. A `.gitignore` file has been created to make sure these files will not be committed, along with other common files.

**April 16 2020:** The template now automatically installs MySQL instead of relying on the Gitpod MySQL image. The message about a Python linter not being installed has been dealt with, and the set-up files are now hidden in the Gitpod file explorer.

**April 13 2020:** Added the _Prettier_ code beautifier extension instead of the code formatter built-in to Gitpod.

**February 2020:** The initialisation files now _do not_ auto-delete. They will remain in your project. You can safely ignore them. They just make sure that your workspace is configured correctly each time you open it. It will also prevent the Gitpod configuration popup from appearing.

**December 2019:** Added Eventyret's Bootstrap 4 extension. Type `!bscdn` in a HTML file to add the Bootstrap boilerplate. Check out the <a href="https://github.com/Eventyret/vscode-bcdn" target="_blank">README.md file at the official repo</a> for more options.

------

## FAQ about the uptime script

**Why have you added this script?**

It will help us to calculate how many running workspaces there are at any one time, which greatly helps us with cost and capacity planning. It will help us decide on the future direction of our cloud-based IDE strategy.

**How will this affect me?**

For everyday usage of Gitpod, it doesn’t have any effect at all. The script only captures the following data:

- An ID that is randomly generated each time the workspace is started.
- The current date and time
- The workspace status of “started” or “running”, which is sent every 5 minutes.

It is not possible for us or anyone else to trace the random ID back to an individual, and no personal data is being captured. It will not slow down the workspace or affect your work.

**So….?**

We want to tell you this so that we are being completely transparent about the data we collect and what we do with it.

**Can I opt out?**

Yes, you can. Since no personally identifiable information is being captured, we'd appreciate it if you let the script run; however if you are unhappy with the idea, simply run the following commands from the terminal window after creating the workspace, and this will remove the uptime script:

```
pkill uptime.sh
rm .vscode/uptime.sh
```

**Anything more?**

Yes! We'd strongly encourage you to look at the source code of the `uptime.sh` file so that you know what it's doing. As future software developers, it will be great practice to see how these shell scripts work.

---

Happy coding!


