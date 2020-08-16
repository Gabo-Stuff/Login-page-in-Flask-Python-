from flask import Flask, render_template, request, make_response
import mysql.connector

# defining the Flask app
app = Flask(__name__)

CONTEXT = {}

# setting the route to execute the code below and the HTTP methods to catch from that route
@app.route("/", methods = ["POST", "GET"])
def login():
    global CONTEXT
    # if get a POST method from the "home.html"
    if request.method == "POST":
        # if user and password fields are both filled
        if request.form.get("login_name") and request.form.get("login_password"):
            user     = request.form["login_name"]
            password = request.form["login_password"]

        # if not filled, display an "error" alert
        else:
            CONTEXT["error_message"] = "User and Password is required"
            return render_template("error_alerts.html", **CONTEXT)

        # verify if the user credentials are passed correctly
        if check_credentials(user, password):
            # set the context with the info to display on the welcome page
            CONTEXT["user_ip"] = request.remote_addr
            CONTEXT["user"] = user

            return render_template("welcome.html", **CONTEXT)

        # if the credentials not match, display an "error" alert
        else:
            CONTEXT["error_message"] = "User or Password not match"
            return render_template("error_alerts.html", **CONTEXT)
    # if not POST anything, just display the html page
    else:
        return render_template("home.html")

# receive the user credentials from the front-end
def check_credentials(user, password):
    # connect to MysqlDB
    mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "password"
    )

    # set the cursor for query
    cur = mydb.cursor()
    # SELECT the login table info
    cur.execute("SELECT * FROM testdb.login")

    # check if the user and password from all rows from the login table match with from the user input 
    for row in cur.fetchall():
        if user == row[0] and password == row[1]:
            return True
        
        else:
            return False
    # end database connection
    mydb.close()

if __name__ == '__main__':
    # run the Flask app
    app.run(debug = True)
