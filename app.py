from flask import *
from database import init_db, db_session
from models import *

app = Flask(__name__)

# TODO: Change the secret key
app.secret_key = "1d45e93cb584e0bb"

# TODO: Fill in methods and routes
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method=="GET":
        return render_template("login.html")
    elif request.method=="POST":
        username=request.form["username"]
        password=request.form["password"]
        print(username)
        print(password)
        #check if the exists by checking if there is a password associated with that username
        #checks if the username is used in the databse and if the user exists
        user = db_session.query(User).where(User.username == username).first()
        if user:
            passcheck = user.password
            #compares the passwords for the second check
            if (password != passcheck):
                flash("Incorrect Username or Password", "login error")
                return redirect(url_for("login"))
            else:
                session["username"] = username
                return redirect(url_for("home"))
        else:
            flash("Incorrect Username or Password", "login error")
            return redirect(url_for("login"))
                
@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method=="GET":
        return render_template("signup.html")
    elif request.method=="POST":
        username=request.form["username"]
        password=request.form["password"]
        passcheck=request.form["passcheck"]
        name=request.form["name"]
        print(username)
        print(password)
        print(passcheck)
        print(name)
        # check if the passwrods match and if the username is already taken
        user = db_session.query(User).where(User.username == username).first()
        if (passcheck != password):
            flash("Passwords do not match", "fail passcheck")
            return redirect(url_for("signup"))
        elif (user):
            flash("That username is taken", "need new username")
            return redirect(url_for("signup"))
        else:
            new_user = User(username, name, password)
            db_session.add(new_user)
            db_session.commit()
            flash("Succesfully Signed Up", "signedup")
            return redirect(url_for("login"))

@app.route("/home")
def home():
    if "username" in session:
        return render_template("home.html")
    else:
        return redirect(url_for("login"))

@app.route("/profile")
def profile():
    if "username" in session:
        user = db_session.query(User).filter(User.username == session["username"]).first()[0]
        tutors = db_session.query(Tutor).all()
        return render_template("profile.html", user=user)
    else:
        return redirect(url_for("login"))

@app.route("/tutor")
def tutor():
    if "username" in session:
        tutors = db_session.query(Tutor).all()
        return render_template("tutorsignup.html", tutors=tutors)
    else:
        return redirect(url_for("login"))

@app.before_first_request
def setup():
    init_db()

if __name__ == "__main__":
    app.run(debug=True)
