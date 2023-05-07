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
        user = db_session.query(User).filter(User.username == session["username"]).first()
        tutorcheck = db_session.query(Tutor).where(Tutor.user_id == user.id).first()
        if(tutorcheck):
            # collects all the information if the user is an tutor and displays it
            # otherwise will display different information based for the user
            comments = db_session.query(RatingTag).where(RatingTag.tutor_id == tutorcheck.id).limit(3).all()
            subjects = tutorcheck.subjects
            return render_template("profile.html", user=user, tutorcheck=tutorcheck, comments=comments, subjects=subjects)
        else:
            comments = db_session.query(RatingTag).where(RatingTag.user_id == user.id).limit(3).all()
            return render_template("profile.html", user=user, tutorcheck=tutorcheck, comments=comments)
    else:
        return redirect(url_for("login"))

@app.route("/tutor", methods=["GET", "POST"])
def tutor():
    if "username" in session:
        user_id = db_session.query(User.id).where(User.username ==session["username"]).first()[0]
        if (request.method == "GET"):
            # takes all of the courses that are available and makes it so that there are available as checkboxes
            courses =[]
            for subject in db_session.query(Subject.name).all():
                courses.append(subject[0])
            return render_template("tutorsignup.html", courses=courses)
        elif (request.method == "POST"):
            # takes all of the requested information and uses that to make a new tutor object
            # takes the list of the classes through the checkboxes and makes subjects tags
            # with the new tutor object in order to link the new tutor to the new subjects
            phone=request.form["phone"]
            email=request.form["email"]
            grade=request.form["grade"]
            bio=request.form["bio"]
            intro=request.form["intro"]
            new_tutor = Tutor(bio, intro, grade, phone, email, user_id)
            db_session.add(new_tutor)
            db_session.commit()
            courses=request.form.getlist("courses")
            print(courses)
            for course in courses:
                new_subject_tag = SubjectTag(new_tutor.id, db_session.query(Subject.id).where(Subject.name == course).first()[0])
                db_session.add(new_subject_tag)
                db_session.commit()
            flash("Succesfully became a tutor", "tutor success")
            return redirect(url_for("tutor"))
    else:
        return redirect(url_for("login"))

@app.route("/review", methods=["GET", "POST"])
def review():
    if "username" in session:
        user_id = db_session.query(User.id).where(User.username ==session["username"]).first()[0]
        if (request.method == "GET"):
            # gives the form a list of all of the tutors so that it can be selected from the drop down list
            tutors = db_session.query(Tutor).all()
            names = []
            for tutor in tutors:
                names.append(db_session.query(User.name).where(User.id == tutor.user_id).first()[0])
            return render_template("comment.html", names=names)
        elif (request.method == "POST"):
            # then it intakes all of the data provided and from that produces the comment that is able to be seen on the
            #  tutors page as well as the user as long as the user isnt a tutor
            tutor_name=request.form["tutor_name"]
            print(tutor_name)
            comment=request.form["comment"]
            tutor = db_session.query(User.id).where(User.name == tutor_name).first()[0]
            tutor_id = db_session.query(Tutor.id).where(Tutor.user_id == tutor).first()[0]
            new_comment = RatingTag(comment, user_id, tutor_id)
            db_session.add(new_comment)
            db_session.commit()
            flash("Submitted Comment", "comment success")
            return redirect(url_for("review"))
    else:
        return redirect(url_for("login"))

#logout
@app.route("/logout")
def logout():
    if "username" in session:
        session.pop("username")
        flash("Succesfully Logged Out", "logged out")
        return redirect(url_for("login"))



@app.before_first_request
def setup():
    init_db()

if __name__ == "__main__":
    app.run(debug=True)
