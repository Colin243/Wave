from database import init_db, db_session
from models import *


init_db()
#subjects that are available
math = Subject("Math")
physics = Subject("Physics")
computer_science = Subject("Computer Science")
chemistry = Subject("Chemistry")
biology = Subject("Biology")
english = Subject("English")
mwh = Subject("Modern World History")
ush = Subject("US History")
euro = Subject("European History")
mandarin = Subject("Mandarin")
spanish = Subject("Spanish")
french = Subject("French")
latin = Subject("Latin")

course_list = [math, physics, computer_science, chemistry, biology, english, mwh, ush, euro, mandarin, spanish, french, latin]
for course in course_list:
    db_session.add(course)
db_session.flush()
# trial data to make sure relationships work
test_user = User("colin243", "colin", "google")
test_user2 = User("gakle", "galen", "google")
test_tutor = Tutor("Test", "Test", 11, "(650)-245-9977", "colin.ho@menloschool.org", db_session.query(User.id).where(User.name == "colin"))
test_tutor2 = Tutor("Test", "Test", 11, "911", "gakle.horch@menloschool.org", db_session.query(User.id).where(User.name == "galen"))
db_session.add(test_user, test_user2)
db_session.add(test_tutor, test_tutor2)
db_session.flush()
test_rating = RatingTag("He's great at tutoring Computer Science!", 4, db_session.query(User.id).where(User.name == "galen"), db_session.query(Tutor.id).where(Tutor.user_id == db_session.query(User.id).where(User.name == "colin")))
test_subject = SubjectTag(db_session.query(Subject.id).where(Subject.name == "Latin"), db_session.query(Tutor.id).where(Tutor.user_id == db_session.query(User.id).where(User.name == "galen")))
db_session.add(test_rating, test_subject)
db_session.flush()



