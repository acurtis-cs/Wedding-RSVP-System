# flask package is used to create my application
from flask import Flask
#Importing this to utilize the flash() funcition
from flask import flash
# tells flask to render the html file (display the html file in the browser)
from flask import render_template
# lets python receive data from the html file.
from flask import request
# lets python redirect to another page after a function is completed.
from flask import redirect
# lets python create a url for the redirect function.
from flask import url_for
# sqlite3 is used to connect to the database I created.
import sqlite3
# Need a secret key that doesn't load into HUB. making an .env file to hold key
# This is the import job is to read that .env file hodling my key.
from dotenv import load_dotenv
#Works fine in terminal, but issues when running .py in IDE
#Having insurance that app works no matter how your running python file.
import os
folder = os.path.dirname(__file__)
#providing the path to my secret key
load_dotenv(os.path.join(folder, ".env"))
#path to my data base
database = os.path.join(folder, "wedding.db")

# creates the actual application
app = Flask(__name__)
#use for other features, but curretnly using it for flash() function to display messages.


# I Now established an actual secret key instead of a demo key for all. hidden in .env file 
app.secret_key = os.environ["SECRET_KEY"]

# this is setting our home page with the /
# methods GET and POST are used to send and receive data from the html file
# function calling the login page html file
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        email = request.form["email"]
        #Now activley enterinlg DB and chekcing email match within data.
        connection = sqlite3.connect(database)
        cursor = connection.cursor()

        cursor.execute(
            "SELECT invite_id FROM guest_emails WHERE email = ?",
            (email,)
        )

        result = cursor.fetchone()
        #Always close the connection of database after grabing data needed.
        connection.close()
        #If no email is found in DB the results just come as none.
        #Use that result to display error message on login page if invalid email is entered.
        if result is None:
            return render_template("login.html", error="Email was not sent an invitation.")
        #Valid email found, retrieve the invite_id.
        invite_id = result[0]

        #Redirect to the dashboard page with the invite_id as a parameter.
        #This allows the dashboard page to know which invitation to display based on the invite_id.
        return redirect(url_for("dashboard", invite_id=invite_id))
    return render_template("login.html")


#Dasboard page fucntion, checks if any of the guests have RSVP. 
# If not redirects to RSVP page (SPRINT 1 LOGIC).
@app.route("/dashboard/<int:invite_id>")
def dashboard(invite_id):

    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    #We obtain the invite_id from login. NOw using that varable again.
    #Need to find the connected guest RSVP status to decided next step.
    cursor.execute(
        "SELECT rsvp_status FROM guests WHERE invite_id = ?",
        (invite_id,)
    )

    results = cursor.fetchall()
    # Closing Alwasy IMPORTANT!!!
    connection.close()
    #True False Variable created
    no_rsvp = False
    #If guest Not Responded turn variable to True
    for row in results:
        if row[0] == "Not Responded":
            no_rsvp = True
            break
    #When variable is True directed to the RSVP Form page. 
    if no_rsvp:
        return redirect(url_for("rsvp", invite_id=invite_id))

    return render_template("dashboard.html")


# RSVP page FORM displays when no RSVP (SPRINT 1 LOGIC )
@app.route("/rsvp/<int:invite_id>", methods=["GET", "POST"])
def rsvp(invite_id):
           
    
    #-------------------------HANDLE RSVP FORM SUBMISSION-----------------------------
    #Handle the RSVP form submission.
    if request.method == "POST":

        #Get information submitted from HTML RSVP form.
        selected_guests = request.form.getlist("guest")
        no_one = request.form.get("no_one")

        #---------------------FAIL SAFE SUBMISSION-----------------------
        #Fail safe after javascript failed, if no guests selected and no_one not checked, return error.
        if len(selected_guests) == 0 and no_one is None:
            #opening database only to get names again
            connection = sqlite3.connect(database)
            cursor = connection.cursor()

            cursor.execute(
                "SELECT guest_id, first_name, last_name FROM guests WHERE invite_id = ?",
                (invite_id,)
            )
            guests = cursor.fetchall()
            connection.close()
            #returning to RSVP page with error message and proper guest names again.
            return render_template(
                "rsvp.html", guests=guests, error="Please select at least one guest or check 'No one is attending'."
            )

        #---------------------UPDATE RSVP STATUS IN DATABASE-----------------------
        #Opening Database to update RSVP from submission.
        connection = sqlite3.connect(database)
        cursor = connection.cursor()

        #PATH if no one is attending
        if no_one is not None:
            cursor.execute(
                "UPDATE guests SET rsvp_status = 'Not Attending' WHERE invite_id = ?",
                (invite_id,)
            )

        #PATH if guest selected to attend
        else:
            #Conductin simple coverage if some guest not selected.
            #Therefore all guest first set to Not Attending.
            cursor.execute(
                "UPDATE guests SET rsvp_status = 'Not Attending' WHERE invite_id = ?",
                (invite_id,)
            )

            #Now updating the selected guests to Attending.
            for guest_id in selected_guests:
                cursor.execute(
                    "UPDATE guests SET rsvp_status = 'Attending' WHERE guest_id = ? AND invite_id = ?",
                    (guest_id, invite_id)
                )
        # Saving changes to the database.
        connection.commit()
        connection.close()
                
        #-------------------- REDIRECT AFTER RSVP ---------------------------

        # If no one is attending, return to dashboard.
        # Simple check
        if no_one is not None:
            flash("RSVP submitted successfully.")
            return redirect(url_for("dashboard", invite_id=invite_id))

        # If guests are attending, send them to Meal Selection Form.
        else:
            flash("RSVP submitted successfully.")
            return redirect(url_for("meal", invite_id=invite_id))

    
    #----------------------- INITIAL PAGE LOAD (GET GUEST)-----------------------
    #entering sql again
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    # using invite_id again to now fetch the names of the guest associated with that invitation.
    cursor.execute(
        "SELECT guest_id, first_name, last_name FROM guests WHERE invite_id = ?",
        (invite_id,)
    )
    #this varble grabes all informaiton we requested above in a list sebreated by tuples.
    guests = cursor.fetchall()
    #CLOSE database connection after fetching guest details!
    connection.close()   
    return render_template("rsvp.html", guests=guests)  #Now here we are sending guests information to guests in HTML




#---------------------------------Meal slection FORM (SPRINT 2 Logic)-----------------------------------------------#
#meal selection form reciving invite_id only
@app.route("/meal/<int:invite_id>")
def meal(invite_id):

    # Open database connection
    connection = sqlite3.connect(database)
    #This is needed since we are placing data into foreign key section
    #We're insuring we don't allow a non submission of a non existing foreign key
    connection.execute("PRAGMA foreign_keys = ON")
    cursor = connection.cursor()

    # Retrieve only attending guests from the current invitation
    # Using SQL instead of carry over so login page can send over as well without needing rsvp()
    cursor.execute(
        "SELECT guest_id, first_name, last_name FROM guests WHERE invite_id = ? AND rsvp_status = 'Attending'",
        (invite_id,)
    )

    guests = cursor.fetchall()

    # Retrieve all meal options
    cursor.execute(
        "SELECT meal_id, meal_name FROM meal_options"
    )

    meal_options = cursor.fetchall()

    # Close database
    connection.close()

    # Send guest names and meal options to HTML
    return render_template(
        "meal.html",
        guests=guests,
        meal_options=meal_options
    )





app.run()