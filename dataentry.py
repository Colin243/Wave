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
db_session.commit()

# test data to make sure relationships work
test_user = User("colin243", "colin", "google")
test_user2 = User("gakle", "galen", "google")
db_session.add_all([test_user, test_user2])
db_session.commit()
test_tutor = Tutor("Test", "Test", 11, "(650)-245-9977", "colin.ho@menloschool.org", db_session.query(User.id).where(User.name == "colin").first()[0])
test_tutor2 = Tutor("Test", "Test", 11, "911", "gakle.horch@menloschool.org", db_session.query(User.id).where(User.name == "galen").first()[0])
db_session.add_all([test_tutor, test_tutor2])
db_session.commit()
test_rating = RatingTag("He's great at tutoring Computer Science!", db_session.query(User.id).where(User.name == "galen").first()[0], db_session.query(Tutor.id).where(Tutor.user_id == db_session.query(User.id).where(User.name == "colin").first()[0]).first()[0])
test_rating2 = RatingTag("Test 2", db_session.query(User.id).where(User.name == "galen").first()[0], db_session.query(Tutor.id).where(Tutor.user_id == db_session.query(User.id).where(User.name == "colin").first()[0]).first()[0])
test_rating3 = RatingTag("Test 3", db_session.query(User.id).where(User.name == "galen").first()[0], db_session.query(Tutor.id).where(Tutor.user_id == db_session.query(User.id).where(User.name == "colin").first()[0]).first()[0])
test_rating4 = RatingTag("Test 4", db_session.query(User.id).where(User.name == "galen").first()[0], db_session.query(Tutor.id).where(Tutor.user_id == db_session.query(User.id).where(User.name == "colin").first()[0]).first()[0])
test_subject = SubjectTag(db_session.query(Tutor.id).where(Tutor.id == 1).first()[0], db_session.query(Subject.id).where(Subject.id == 13).first()[0])
test_subject2 = SubjectTag(db_session.query(Tutor.id).where(Tutor.id == 1).first()[0], db_session.query(Subject.id).where(Subject.id == 1).first()[0])
test_subject3 = SubjectTag(db_session.query(Tutor.id).where(Tutor.id == 1).first()[0], db_session.query(Subject.id).where(Subject.id == 12).first()[0])
test_subject4 = SubjectTag(db_session.query(Tutor.id).where(Tutor.id == 1).first()[0], db_session.query(Subject.id).where(Subject.id == 3).first()[0])
test_subject5 = SubjectTag(db_session.query(Tutor.id).where(Tutor.id == 1).first()[0], db_session.query(Subject.id).where(Subject.id == 4).first()[0])
db_session.add_all([test_rating, test_rating2, test_rating3, test_rating4, test_subject, test_subject2, test_subject3, test_subject4, test_subject5])
db_session.commit()