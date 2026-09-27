# flask package is used to create my application
from flask import Flask
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
#Works fine in terminal, but issues when running py in IDE
#Having insurance that app works no matter how your running python file.
import os
folder = os.path.dirname(__file__)
database = os.path.join(folder, "wedding.db")

# creates the actual application
app = Flask(__name__)

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
    no_rsvp = True
    #If guest responded turn variable to False
    for row in results:
        if row[0] != "Not Responded":
            no_rsvp = False
    #When variable is True directed to the RSVP Form page. 
    if no_rsvp:
        return redirect(url_for("rsvp", invite_id=invite_id))

    return render_template("dashboard.html")


# RSVP page FORM displays when no RSVP (SPRINT 1 LOGIC )
@app.route("/rsvp/<int:invite_id>", methods=["GET", "POST"])
def rsvp(invite_id):
    #Handle the RSVP form submission.
    if request.method == "POST":
        selected_guests = request.form.getlist("guest")
        no_one = request.form.get("no_one")

        print(selected_guests)
        print(no_one)
    
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

app.run()