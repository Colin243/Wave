"""
The file that holds the schema/classes
that will be used to create objects
and connect to data tables.
"""

from sqlalchemy import ForeignKey, Column, INTEGER, TEXT
from sqlalchemy.orm import relationship
from database import Base

# TODO: Complete your models

class User(Base):
    __tablename__ = "users"
    # TODO: Complete the class
    id = Column("id", INTEGER, primary_key=True)
    username = Column("username", TEXT, nullable=False)
    name = Column("name", TEXT, nullable=False)
    password = Column("password", TEXT, nullable=False)
    tutors = relationship("Tutor", secondary="ratingtags", back_populates="users")

    def __init__(self, username, name, password):
        self.name = name
        self.password = password
        self.username = username

class Tutor(Base):
    __tablename__ = "tutors"
    # TODO: Complete the class
    id = Column("id", INTEGER, primary_key=True)
    bio = Column("bio", TEXT, nullable=False)
    intro = Column("intro", TEXT, nullable=False)
    grade = Column("grade", TEXT, nullable=False)
    phone = Column("phone", TEXT, nullable=False)
    email = Column("email", TEXT, nullable=False)
    user_id = Column(INTEGER, ForeignKey('users.id'), nullable=False)
    users = relationship("User", secondary="ratingtags", back_populates="tutors")
    subjects = relationship("Subject", secondary="subjecttags", back_populates="tutors")

    def __init__(self, bio, intro, grade, phone, email, user_id):
        self.bio = bio
        self.intro = intro
        self.grade = grade
        self.phone = phone
        self.email = email
        self.user_id = user_id


class RatingTag(Base):
    __tablename__ = "ratingtags"
    # TODO: Complete the class
    id = Column("id", INTEGER, primary_key=True)
    comment = Column("comment", TEXT, nullable=False)
    user_id = Column(INTEGER, ForeignKey('users.id'))
    tutor_id = Column(INTEGER, ForeignKey('tutors.id'))

    def __init__(self, comment, user_id, tutor_id):
        self.comment = comment
        self.user_id = user_id
        self.tutor_id = tutor_id
    
    def __repr__(self):
        return self.comment

class Subject(Base):
    __tablename__ = "subjects"
    # TODO: Complete the class
    id = Column("id", INTEGER, primary_key=True)
    name = Column("name", TEXT, nullable=False)
    tutors = relationship("Tutor", secondary="subjecttags", back_populates="subjects")

    def __init__(self, name):
        self.name = name


class SubjectTag(Base):
    __tablename__ = "subjecttags"
    # TODO: Complete the class
    id = Column("id", INTEGER, primary_key=True)
    tutor_id = Column(INTEGER, ForeignKey('tutors.id'))
    course_id = Column(INTEGER, ForeignKey('subjects.id'))

    def __init__(self, tutor_id, course_id):
        self.tutor_id = tutor_id
        self.course_id = course_id