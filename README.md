# Wedding RSVP Management System

## Creator: Alex Curtis

## Project Objective
Build a Wedding RSVP Management System that allows invited guests to log in using an authorized email, submit and manage RSVP responses, and select meals for the wedding reception.

## Updated Sprint 2 Goal (11/01/2026)
Allow wedding guests to select meals for attending guests, view current RSVP statuses and meal selections, attendance totals, meal totals, sorting, and filtering to easily review wedding guest information.


## Sprint 2 Goal (10/23/2026)
Allow a wedding guest to select meals for their party, view updated RSVP statuses and meal selections within their respectable tabs.

## Sprint 1 Goal
Allow a wedding guest to log in, view the guests associated with their invitation, and submit an RSVP indicating who is attending or that no one is attending.

### Technologies:
- Python 3.13.14
- pytest 9.2.0
- Flask 3.1.3 
- python-dotenv 1.2.4
- SQLite 
- HTML
- CSS
- JavaScript
- Node.js 26.13.0
- npm 11.20.0
- Vitest 5.1.0
- jsdom 31.0.0



### Prerequisites

- Python 3.13.14 or compatible version to run requirements
- Node.js with npm for JavaScript automated testing. Download Node.js from https://nodejs.org/en/download (npm is included).
- Git to clone
- DB Browswer for SQLite 3.13.1 for managing database values.


### Installation

1. Clone repository from GitHub using: git clone https://github.com/acurtis-cs/Wedding-RSVP-System.git

2. Open the Wedding-RSVP-System project folder in VS Code or another code editor.

3. Open a Windows PowerShell terminal in the project folder containing app.py. 

4. Install the required Python packages in terminal using: python -m pip install -r requirements.txt

5. Install the JavaScript testing packages in terminal using: npm.cmd ci
    - NOTE: Node.js and npm are only needed for JavaScript automated testing. 


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


### Trying the Sprint 2 Functionality

The following steps are reviewer instructions for user stories completed during Sprint 2.

- Meal Selection Form
    1. Open the application and log in using a registered guest email.
    2. Complete the RSVP form and select at least one attending guest.
    3. After submitting the RSVP, the Meal Selection Form automatically appears.
    4. Verify that only attending guests are displayed.
    5. Attempt to submit without selecting a meal for every guest. Verify submission is prevented.
    6. Select a meal for each attending guest and submit.
    7. Verify that a confirmation message appears and the application returns to the dashboard.
    8. Confirm completed meal selections in DB with DB Browser SQLite.

- RSVP Guest List
    1. Log in using an invitation with completed RSVP information.
    2. Select the RSVP Guest List button on the dashboard.
    3. Verify that the current invitation's guests appear in the Your Invitation section.
    4. Verify that all invited guests are displayed in the All Invited Guests section.
    5. Confirm that Attending, Not Attending, and Not Responded statuses are displayed correctly.
    6. Log in using a different invitation to verify that the Your Invitation section changes accordingly.

- Meal Selection List
    1. Select the Meal Selection List button from the dashboard.
    2. Verify that the Your Meals section displays the current invitation's attending guests with saved meals.
    3. Verify that the All Meal Selections section displays attending guests with saved meal selections.
    4. Confirm that nonattending guests do not appear in the meal list.
    5. Verify that each guest's selected meal is displayed correctly.

- RSVP Attendance Totals
    1. Log in using an invitation with completed RSVP and meal information, if applicable.
    2. Verify you're on the dashboard page.
    3. Verify that the RSVP Status Totals section displays Total Invited, Attending, Not Attending, and Not Responded.
    4. Verify that the totals are accurate with current guest records in the database.
    5. After changing RSVP data through the normal submission workflow, return to the dashboard and verify that the totals reflect the saved information.


- Meal Selection Totals
    1. Log in using an invitation with completed RSVP and meal information, if applicable.
    2. Select the Meal Selection List button from the dashboard.
    3. Verify that the Meal Selection Totals section displays each available meal and its total selections.
    4. Confirm the totals are accurate with current meal selection records in the database.
    5. Verify that meals with no selections display a total of zero.
    6. After submitting additional meal selections, return to the Meal Selection List and verify that the totals reflect the saved information.

- RSVP Guest List Sorting and Filtering
    1. Open the RSVP Guest List.
    2. Click 'ALL invitations' Guest Name once to sort alphabetically by first name, symbol (↑).
    3. Click again to sort in reverse alphabetical order, symbol (↓), then a third time to restore the original order, symbol (-).
    4. Select a status from the RSVP Status dropdown to display only guests with that status.
    5. Verify that sorting continues to work while a filter is selected.
    6. Select RSVP Status again in dropdown to restore all guests.
    
- Meal Selection List Sorting and Filtering
    1. Open the Meal Selection List.
    2. Click 'ALL invitations' Guest Name once to sort alphabetically by first name, symbol (↑).
    3. Click again to sort in reverse alphabetical order, symbol (↓), then a third time to restore the original order, symbol (-).
    4. Select a meal from the Meal Selection dropdown to display only guests with that meal.
    5. Verify that sorting continues to work while a filter is selected.
    6. Select Meal Selection again in dropdown to restore all meal selections.



### Automated Testing (Sprint 2)

The application uses pytest to perform automated tests of the new Sprint 2 logic.

- Running Python Automated Tests
    1. Open a Windows PowerShell terminal in the Wedding-RSVP-System project folder containing `calculations.py`.
    2. Install the required dependencies using `python -m pip install -r requirements.txt`.
    3. Run the automated tests using `python -m pytest -v` in terminal.
    4. Review the terminal output to confirm all automated tests pass.

- Running JavaScript Automated Tests
    1. Open a Windows PowerShell terminal in the Wedding-RSVP-System project folder containing `package.json`.
    2. Verify Node.js and npm are installed using `node -v` and `npm.cmd -v`.
    3. Install the JavaScript testing dependencies using `npm.cmd ci`.
    4. Run the automated tests using `npm.cmd test`.
    5. Review the terminal output to confirm all automated tests pass.


**Attendance Totals Tests**
- Test File: `tests/test_rsvp_totals.py`
    1. `test_rsvp_totals`: Verifies that total invited, attending, not attending, and not responded guests are counted correctly.
    2. `test_empty_guest_list`: Verifies that an empty guest list produces zero for all attendance totals.
    3. `test_updated_rsvp_totals`: Verifies that attendance totals are recalculated correctly when RSVP information changes.


**Meal Selection Totals Tests**
- Test File: `tests/test_meal_totals.py`
    1. `test_meal_totals`: Verifies that saved meal selections are counted correctly, including meals with zero selections.
    2. `test_empty_meal_selections`: Verifies that no saved meal selections produce zero for all available meal totals.
    3. `test_updated_meal_totals`: Verifies that meal totals are recalculated correctly when additional meal selections are added.

**Sorting and Filtering Tests**
- Test File: `tests/list_sort_filter.test.js`
  1. `RSVP sorting cycles through all three states`: Verifies original, alphabetical, reverse alphabetical, and restored order.
  2. `RSVP filtering shows only matching guests`: Verifies that the dropdown displays matching RSVP statuses and can restore all rows.
  3. `Meal List sorting and filtering works`: Verifies meal selection filtering and alphabetical sorting together.
  4. `Empty table works without errors`: Verifies that an empty table does not cause errors during sorting or filtering.


The Python tests use sample guest records and meal selections. The JavaScript tests create a sample HTML table and load `list-sort.js` and `list-filter.js` files using jsdom. These automated tests do not modify or access the application's `wedding.db` database.

The automated tests verify the calculation, sorting, and filtering logic. Dashboard and Meal Selection List displays with database integration and database results are checked manually as part of verification testing.

### Known limitations

Current abilities of the application allow guests to submit RSVP responses, select meals, view RSVP and meal information, and sort or filter guest and meal list. Users can't delete or edit RSVP or meals after submission. Application currently has no user ability to initiate RSVP or meal selection, the system atomically initiates RSVP form then meal form after login if user’s party has RSVP status “Not Responded” or RSVP status "Attending" with no meal selection. Meal options must be managed directly in SQLite. Login currently uses an authorized email without password authentication.

