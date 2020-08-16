# Login-page-in-Flask-Python-
The code runs a local server made in Python with Flask, which connects to a MySQL database to display an HTML web page styled with CSS.

file tree:

static (folder)
  - style.css
  
templates (folder)
  - home.html
  - welcome.html
  - error_alerts.html
  
server.py

In "server.py" runs the server and checks if a POST or GET method arrives from http://127.0.0.1:5000/.
If GET, display "home.html".
If POST check the User and Password fields (from "home.html"), if both filled (if not, alerts an error) checks if match with those same fields in the MySQL login table.
If doesn't match, alerts an error. If matches, redirects to "welcome.html".

(To execute the code needs the correct file tree and an MySQL testdb.login table)
