# Wedding RSVP Management System

## Creator: Alex Curtis

## Project Objective
Build a Wedding RSVP Management System that allows invited guests to log in using an authorized email, submit and manage RSVP responses, and select meals for the wedding reception.

## Sprint 1 Goal
Allow a wedding guest to log in, view the guests associated with their invitation, and submit an RSVP indicating who is attending or that no one is attending.

### Technologies:
- Python 3.13.14
- Flask 3.1.3 
- python-dotenv 1.2.4
- SQLite 
- HTML
- CSS
- JavaScript


### Prerequisites

- Python 3.13.14 or compatible version to run requirements
- Git to clone
- DB Browswer for SQLite 3.13.1 for managing database values.


### Installation

1. Clone repository from GitHub using: git clone https://github.com/acurtis-cs/Wedding-RSVP-System.git

2. Open the Wedding-RSVP-System project folder in VS Code or another code editor.

3. Open a Windows PowerShell terminal in the project folder containing app.py. 

4. Install the required Python packages in terminal using: python -m pip install -r requirements.txt


### Configuration

This application requires a Flask secret key stored in a local .env file.
1. Two ways creating your .env file.
    - One: Create a copy of .env.example and name the copy .env. using command: Copy-Item .env.example .env
    - Two: Or just rename file .env.example to .env

2. Generate a Random Secret key by running command: python -c "import secrets; print(secrets.token_hex(32))"

3. Open .env file and replace the placeholder value with your generated key:
    - SECRET_KEY=[place-key-right-here-take-off-brackets-too]

4. Save the file.
.env file will not push to GitHub due to being in the .gitignore file.

DB Browser SQLite must have guest rsvp_status as "Not Responded" for sprint 1 to work
1. Open file wedding.db using application DB Browser for SQLite.

2. Click “Browse Data” tab, click the drop down setting for “Table:” and choose “guest_invite_view”.

3. Examine guest rsvp_status and confirm column says, “Not Responded” (Application case sensitive). Also review emails for email login credentials.

4. If rsvp_status is not in desire state click “Execute SQL” tab.

5. Place command: UPDATE guests SET rsvp_status = 'Not Responded';

6. Click “Execute all” and then save your changes by clicking “Write Changes”
This saves your database information in the desire state to test Sprint 1. 



### Running the application.
1. Open a terminal in project folder containing app.py or open foler in VS code
2. Run: python app.py
3. Open a web browser and visit: http://127.0.0.1:5000 or click link address in terminal
4. Wedding RSVP login page will appear.
5. To STOP the Flask application, press Ctrl + C in the terminal.


### Tyring the Sprint 1 Functionality

The following steps are reviewer instructions for user stories completed during Sprint 1.

- Guest Login
    1. Open the application login page.
    2. Enter a registered email from wedding.db.
    3. Submit email.
    4. Confirm the correct invitation is loaded.
    5. Try an unregistered email and confirm an error appears.
    6. Attempt to submit a blank email field to verify HTML validation.

- View Associated Guests
    1. Log in with an invitation whose RSVP status is "Not Responded".
    2. Verify that the RSVP form automatically appears.
    3. Confirm all guests associated with that invitation are displayed.
    4. Verify each guest has a selectable checkbox.

- Submit RSVP
    1. Attempt submission without selecting anything. Verify that an error appears.
    2. Select one or more guests as attending.
    3. Submit the RSVP form.
    4. Verify the submission confirmation appears.
    5. Check that attendance statuses are saved correctly in wedding.db.
    6. Log in again to confirm the saved information behaves accordingly.

- Decline Entire Invitation
    1. Use an invitation with RSVP status "Not Responded".
    2. Select "No one is attending".
    3. Verify all individual guest checkboxes become unchecked and disabled.
    4. Uncheck "No one is attending" and verify the individual checkboxes enable again.
    5. Select "No one is attending" and submit.
    6. Verify all associated guests are saved as "Not Attending".
    7. Confirm the application returns to the dashboard.

### Known limitations

Sprint 1 only focuses on the initial guest login and RSVP submission workflow. Users can't see their RSVP status, delete or edit them after submission. Meal’s selection is not available or status given yet. Viewing any database information is done through SQLight. Application currently has no user ability to initiate RSVP selection, the system atomically initiates RSVP form after login if user’s party has RSVP status “Not Responded”

