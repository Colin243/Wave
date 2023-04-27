from flask import *
from database import init_db, db_session
from models import *

app = Flask(__name__)

# TODO: Change the secret key
app.secret_key = "Change Me"

# TODO: Fill in methods and routes
@app.route("/")
def login():
    return render_template("login.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/profile")
def profile():
    return render_template("tutorprofile.html")

@app.route("/tutor")
def tutor():
    return render_template("tutorsignup.html")

@app.before_first_request
def setup():
    init_db()

if __name__ == "__main__":
    app.run(debug=True)