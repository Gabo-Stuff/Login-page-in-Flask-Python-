# Login-page-in-Flask-Python-
The code runs a local server made in Python with Flask, which connects to a MySQL database to display an HTML web page styled with CSS.

file tree:

static(folder)
  - style.css
  
templates(folder)
  - home.html
  - welcome.html
  - error_alerts.html
  
server.py

In "server.py" runs the server and checks if a POST or GET method arrives from http://127.0.0.1:5000/.
If GET, display "home.html".
If POST check the User and Password fields, if both filled (if not, alerts an error) checks if match with those same fields in the MySQL login table.
If doesn't match alerts an error. If match, redirects to "welcome.html".
