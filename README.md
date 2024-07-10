# NeatNotes ReadME

## Introduction

Welcome to NeatNotes, a clean and simple app where user experience is paramount.

![Screenshot of site](static/images/readmeintro.png)

[Deployed Site](https://neatnotes-273c093a6f6f.herokuapp.com/neat/notes/)

## Agile Approach
An Agile approach was taken in the planning and production of the app. This entailed identifying themes which helped to create user stories that attempt to capture the needs and desires of the user in relation to the app. Once identified, the user stories were added to a Kanban board: a place to organise and keep track of tasks. Due to the tight deadline, it was important to remain true to the Agile methodology, and complete the basic needs before moving onto less important functionality and style.

![Kanban board](static/images/kanban.png)

## User Stories
**As a user I want to create a note to help keep my life organised.**

Acceptance Criteria:
- button to create a note
- interface for user input of title and text
- button to save note

**As a user I want to be able to view my saved notes, so that I can come back to them in the future.**

Acceptance Criteria:
- menu of saved notes.
- note loads when click on title in menu

**As a user I want to be able to update my notes, so that I can make changes to them.**

Acceptance Criteria:
- When user clicks on a note there will be an edit button, making the text and title editable
- Save button will update the note

**As a user I want to be able to delete a note so that I can get rid of old notes I don't need anymore.**

Acceptance Criteria:
- Button to delete note
- Alert to confirm deletion or go back

**As a user I want to be able to login so that I can privately view, create, update and delete my personal notes.**

Acceptance Criteria:
- Front end form to input login details
- Login details checked backend
- Messages to tell user if the email/password is incorrect
- Submit button

**As a user I want to be able to register so that I can create an account and login in the future.**

Acceptance Criteria:
- Front end form for user details
- Account created upon form submission
- User can login next time

**As a user I want a site that is clearly laid out so that I can see my notes clearly.**

Acceptance Criteria:
- Clean, simple frontend layout for easy reading
- Buttons purpose are either labelled or otherwise obvious

**As a user I want to be able to navigate the site easily so that I have a better user experience.**

Acceptance Criteria:
- Clear buttons to bring up a list of saved notes
- Clicking on a note title will bring it up
- Clear logout button

**As a user I want to be able to label a note as important, so that I can see my more important notes in one place.**

Acceptance Criteria:
- Star button next to each note to mark as important
- Important notes added to new set in the backend
- Button to undo important label and send back to normal notes

**As a site owner, I want a nice logo and distinctive colours to advertise my brand.**

Acceptance Criteria:
- Well designed logo
- Harmonious colour palette chosen

**As a user I want to be able to share my notes, so that others can view them.**

Acceptance Criteria:
- Share button next to save button
- Functionality implemented to email note to others

## Wireframes

I created wireframes on Balsamiq in order to visualise the layout of the site. While the finished product differs from the wireframes quite significantly, they still served me well as a 
rough guide.

[Link to wireframes document](docs/wireframes.bmpr)



## Workflow

I created a site map and workflow diagram: **CHANGE THIS ONCE DONE**

![Screenshot 2023-12-07 at 14 12 33](https://github.com/rachbry/recipme-django-cookbook/assets/73660517/c5ed706d-1b01-4a22-8e40-6e4ff5511e61)

## Features



### Models
I used the Django AllAuth User Model and created a custom model. This included the following fields:

|      Name            |     Type                   |     Key  |
|----------------------|----------------------------|----------|
|      user            |     User Model             |     FK   |
|      title           |     CharField              |          | 
|      text            |     CharField  dropdown    |          |
|      Created         |     CharField  dropdown    |          |
|      is_important    |     Boolean                |          |

## Design
### Wireframes and Features
The site is be fully responsive and accessible on mobile, tablet and desktop devices.

![Screenshot 2023-12-07 at 13 50 23](https://github.com/rachbry/recipme-django-cookbook/assets/73660517/112af580-6678-4e52-b3f3-76db12c4f240)

**All Users:**
- Are able to view admin added recipes
- Are able to use the search functionality

**Logged In Users:**
- Can add recipes
- Can view, edit and delete their own recipes
- Can add recipes to their favourites
  
They will have a personalised home page with all their recipes on it and will be able to view recipes they have favourited, both from their own and the site recipe collections.  Each recipe card will be a clickable link to the full recipe.  The same page layout will be used for the recipe collection, the users homepage and the favourite recipes page to maintain consistency and simplicity throughout.

![Screenshot 2023-12-07 at 13 33 50](https://github.com/rachbry/recipme-django-cookbook/assets/73660517/f688c986-8040-48cb-938a-64b20b189f72)



**The Full Recipe Page:**
Will contain all the relevent information for each recipe.  Design will ensure all ingredients and instructions are available on one screen for desktop and tablet.

![Screenshot 2023-12-07 at 13 36 14](https://github.com/rachbry/recipme-django-cookbook/assets/73660517/3e8edc07-582b-41de-8cd6-6ce59475f3be)



**Add / Edit Recipe Page:**
Front End CRUD will be available to add / edit recipes for logged in users.  The form will include category dropdowns and the ability to upload an image.

![Screenshot 2023-12-07 at 13 42 11](https://github.com/rachbry/recipme-django-cookbook/assets/73660517/42943578-41c6-4061-b0e4-e9debaa239bd)


## Design Choices
###  Colours

I used [coolors.co] (https://coolors.co/palette/253439-ff5757-545454-ffbd59-f5f4f3) to generate my colour palette:

![image](https://github.com/rachbry/recipme-django-cookbook/assets/73660517/027c781a-346b-4ed8-93ed-9a42815c0f0f)

I aimed for a clean and simple website design that keeps the focus on the content. Opting for a vibrant colour scheme, I wanted to strike a balance between minimalism and boldness. The light off-white background (#f5f4f3) keeps things simple and clean, while introducing splashes of colour add a touch of visual interest that contrasts against the neutral backdrop. This combination creates a modern look without being too over the top.

Coral and yellow form a complementary pairing, and their warmth complemented by cool grey tones, ensures a visually cohesive and balanced palette.  The neutral colours help maintain an overall sense of harmony.

The result is a carefully chosen color palette that enhances the design without overwhelming it, adding sophistication and vibrancy.

### Branding

![image](https://github.com/rachbry/recipme-django-cookbook/assets/73660517/ea618f02-99f6-4947-a764-8ffe40bb4155)

### Typography

I created a logo on Canva using Josefin Sans, and used this for the headers and titles in my website for continuity of design.  While Josefin Sans has a geometric feel I paired this with Lato for a modern, clean appearance.  This pairing ensures readability, making text clear and easy to read. The fonts are versatile, suitable for various contexts like web and print designs. Despite their unique characteristics, they maintain consistency in proportions and weights, contributing to a cohesive and professional look. The combination strikes a balance, creating an aesthetically pleasing design that blends the vintage charm of Josefin Sans with the clean modernity of Lato.



## RecipMe

### Homepage

![Screenshot 2023-12-08 at 12 03 20](https://github.com/rachbry/recipme-django-cookbook/assets/73660517/7abfbfb0-59bd-4442-b208-c1ee634a79dd)


### Sign In

![Screenshot 2023-12-08 at 12 09 17](https://github.com/rachbry/recipme-django-cookbook/assets/73660517/ffcb1ee2-5192-4d04-8a76-0dd7d61798ea)


### Add / Edit Pages

![Screenshot 2023-12-08 at 12 20 19](https://github.com/rachbry/recipme-django-cookbook/assets/73660517/62545a43-e46b-41b8-95e3-9edece069e07)


### RecipMe, Favourites

![Screenshot 2023-12-08 at 12 30 57](https://github.com/rachbry/recipme-django-cookbook/assets/73660517/af2e5cb7-a489-4239-96bb-fbb5e76963b4)


![Screenshot 2023-12-08 at 12 35 16](https://github.com/rachbry/recipme-django-cookbook/assets/73660517/6fdb2dd1-56c0-4c7f-9388-f22b00e5368b)


###  Personalised Home Page 

![Screenshot 2023-12-08 at 12 40 17](https://github.com/rachbry/recipme-django-cookbook/assets/73660517/2049f4cc-a85e-4ed7-9010-0197f17aac23)


### Full Recipe Page

![Screenshot 2023-12-08 at 12 46 15](https://github.com/rachbry/recipme-django-cookbook/assets/73660517/9e79d26c-09d0-43ac-96e4-cc291166ec50)




### Future Features
Future features not implemented at this time include:
- The ability on the full recipe page to toggle on/off dark mode and prevent your screen turning off, a feature I feel would be very useful when following a recipe
- Recipe sharing - To be able to share recipes with other users of the site or to email them to others
- Upload recipes to main site - The ability to request admin approval for a recipe to be added to the site wide collection
- Notes - the ability for a user to leave notes on their recipes outlining any tweaks they may have made


## Testing

Results of manual testing:
[Testing](testing.md)

## Responsiveness
This website has been tested and is fully responsive on Desktop, Mac book, Ipad and mobile devices.

                                      

## Browser Compatibility

The website has been tested and is being displayed as expected on Safari, Google Chrome and Firefox as well as on android and apple devices.

| Screenshots                                                                                                                                      | Ipad and Iphone SE                                                                                                   |
|--------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|
| ![53d76d73-ebe8-46ee-9860-8137adc34f04](https://github.com/rachbry/recipme-django-cookbook/assets/73660517/18cdc571-d3ce-4f13-972f-9b7e98cd6936) | ![ipad](https://github.com/rachbry/recipme-django-cookbook/assets/73660517/6124121e-03e9-4085-9200-746d3aa4812c)     |
| ![IMG_0144](https://github.com/rachbry/recipme-django-cookbook/assets/73660517/62afc582-cedd-4e03-802c-9afeeb5f1c8d)                             | ![IMG_0143](https://github.com/rachbry/recipme-django-cookbook/assets/73660517/ae16c7b3-08dc-4077-8fe7-b314cd527072) |

## Bugs
- On the edit recipe page there is no success message appearing.  It does reload the page if successful and return to the top of page
- The only feature not currently working is the 'forgot your password' link, email authentication was out of scope for this project.


## Technologies Used
- CSS
- Django
- HTML
- Bootstrap
- Python
- ElephantSQL Postgres Database
- Cloudinary - All user submitted recipe photos are uploaded to cloudinary

- GitPod development environment used
- GitHub used for version control and code hosting
- GitHub Projects used for Agile Methodology

## Deployment
- I followed the following screenshot to deploy my project to Heroku:

![image (2)](https://github.com/rachbry/recipme-django-cookbook/assets/73660517/26d212cb-0a51-4bb3-8485-d2fb189eebdc)


# Credits

- The Structure of my website was based around this tutorial with Dee Mc:
https://youtu.be/JzDBCZTgVyw?si=w3BBwJswUjBTm1xw 
- This tutorial was used to assist in the creation of my favourite button:
https://www.youtube.com/watch?v=H4QPHLmsZMU
- ChatGPT was used for troubleshooting, bug fixing and content generating.  Also used to create my persona.
- Thanks to Stacey Robson for the Heroku deployment guide
- Thanks to the other members of the Bootcamp for their technical and moral support
- Recipes used were from the bbc good food website
- Hero on image home page retrieved ella-olsson-KPDbRyFOTnE-unsplash.jpg https://images.unsplash.com
- Fontawesome was used for icons
- Google fonts was used
- Wireframes created in Balsamiq
- Logo and flow chart created in Canva
