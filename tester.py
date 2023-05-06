from database import init_db, db_session
from models import *


init_db()
comments = db_session.query(RatingTag.comment).where(RatingTag.tutor_id == 1).limit(3).all()
for comment in comments:
    print(comment)
user = db_session.query(Tutor).where(Tutor.id == 1).first()
user2 = db_session.query(User).where(User.id == 1).first()
subjects = user.subjects
for subject in subjects:
    print(subject.name)
tutors = db_session.query(Tutor).all()
print(tutors)
names = []
for tutor in tutors:
    name = (db_session.query(User.name).where(User.id == tutor.user_id).first())
    print(name)
    names.append(name)
print(names)

tutor = db_session.query(User.id).where(User.name == "galen").first()[0]
print(tutor)
tutor_id = db_session.query(Tutor.id).filter(Tutor.user_id == tutor).first()[0]
print(tutor_id)
