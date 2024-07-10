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

**As a user, I want to be able to logout, so I know my notes are secure when I am not using the app.**

Acceptance Criteria:
- Button for logging out
- Confirmation message when logged out
- No access to site until logged in again

**As a user I want to be able to register so that I can create an account and login in the future.**

Acceptance Criteria:
- Front end form for user details
- Account created upon form submission
- User can login next time

**As a user I want a site that is clearly laid out so that I can see my notes clearly.**

Acceptance Criteria:
- Clean, simple frontend layout for easy reading
- Buttons purpose are either labelled or otherwise obvious

**As a user I want to be able to navigate the site easily, so that I have a better user experience.**

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

## Planning

### Wireframes

I created wireframes on Balsamiq in order to visualise the layout of the site. While the finished product differs from the wireframes quite significantly, they still served me well as a 
rough guide. Some features shown in the wireframes have not been implemented due to a lack of time. The design is simple as I believe a notes app should be, using only black and white, and 
with no intrusive content on the page.

[Link to wireframes document](docs/wireframes.bmpr)

### Workflow

I created workflow diagram to help me understand the path a user would take on the site, as well as the required logic to implement it.

![Screenshot of Workflow diagram](static/images/workflow.png)

### Models
I created a custom model with the following fields:

|      Name            |     Type                   |     Key  |
|----------------------|----------------------------|----------|
|      user            |     User Model             |     FK   |
|      title           |     CharField              |          | 
|      text            |     CharField  dropdown    |          |
|      Created         |     CharField  dropdown    |          |
|      is_important    |     Boolean                |          |

### Capstone Project Planning

I used dbdiagrams to define my database tables. It was useful as an overview of the database, and served me well as a reference while working on the backend logic.

![Screenshot of database diagram](static/images/databasediagram.png)

#### Planning my Django Apps and Views

##### App: Home

###### Models: User

###### Views

- SignupView: handles user registration.
- LoginInterfaceView: sends user to homepage when logged in.
- LogoutInterfaceView: sends user to logout page when logging out.
- HomeView: logged in users sent to home

##### App: notes

##### Models: Notes

##### Views

- NotesDeleteView: allows user deletion of notes.
- NotesUpdateView: allows user editing notes.
- NotesCreateView: allows user to create a note.
- NotesListView: handles template to view notes.
- NotesDetailView: handles template to view note detail.
- toggle_important: handles note important status.

### Features

#### Register

New users are able to register with a username and password, allowing them to login and create notes privately.

![screenshot of registration](static/images/signup.png)

**Related User Story: As a user I want to be able to register so that I can create an account and login in the future.**
**Testing: pass.**


#### Login

Registered users can login using the form, allowing them access to the site.

![screenshot of login form](static/images/login.png)

Users are notified when they login:

![screenshot of notification](static/images/loginmessage.png)

**Related User Story: As a user I want to be able to login so that I can privately view, create, update and delete my personal notes.**
**Testing: pass.**

#### Logout 

Logged-in users can securely logout.

![screenshot of logout in navbar](static/images/logoutnavbar.png)

Users are given confirmation of logging out and a thank you message. There is no django notification as it is already in the template.

![screenshot of logout message](static/images/logoutmessage.png)

**Related User Story: As a user, I want to be able to logout, so I know my notes are secure when I am not using the app.**
**Testing: pass.**


#### Create Note

Users can create and save notes. They can either use the navbar...

![screenshot of creating note from navbar](static/images/createnavbar.png)

... or the plus sign to do this.

![screenshot of creating note with plus](static/images/create.png)

**Related User Story: As a user, I want to create a note to help keep my life organised.**
**Testing: pass.**

#### Delete Note

Users can delete notes they no longer need or want.

![screenshot of delete button](static/images/delete.png)

 There is a confirmation message to ensure no accidental deletions.

 ![screenshot of delete confirmation](static/images/deleteconfirm.png)

**Related User Story: As a user I want to be able to delete a note so that I can get rid of old notes I don't need anymore.**
**Testing: pass.**









