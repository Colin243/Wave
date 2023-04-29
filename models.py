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
    tutors = relationship("Tutor", secondary="commenttags", back_populates="users")

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
    status = Column("status", TEXT)
    rating = Column("rating", INTEGER) 
    user_id = Column(INTEGER, ForeignKey('users.id'))
    users = relationship("User", secondary="commenttags", back_populates="tutors")
    courses = relationship("Course", secondary="coursetags", back_populates="tutors")

    def __init__(self, bio, intro, grade, phone, email):
        self.bio = bio
        self.intro = intro
        self.grade = grade
        self.phone = phone
        self.email = email


class CommentTag(Base):
    __tablename__ = "commenttags"
    # TODO: Complete the class
    id = Column("id", INTEGER, primary_key=True)
    comment = Column("comment", TEXT, nullable=False)
    user_id = Column(INTEGER, ForeignKey('users.id'))
    tutor_id = Column(INTEGER, ForeignKey('tutors.id'))

    def __init__(self, comment, user_id, tutor_id):
        self.comment = comment
        self.user_id = user_id
        self.tutor_id = tutor_id

class Course(Base):
    __tablename__ = "courses"
    # TODO: Complete the class
    id = Column("id", INTEGER, primary_key=True)
    name = Column("name", TEXT, nullable=False)
    honors = Column("honors", bool, nullable=False)
    ap = Column("ap", bool, nullable=False)
    tutors = relationship("Tutor", secondary="coursetags", back_populates="courses")


class CourseTag(Base):
    __tablename__ = "coursetags"
    # TODO: Complete the class
    id = Column("id", INTEGER, primary_key=True)
    tutor_id = Column(INTEGER, ForeignKey('tutors.id'))
    course_id = Column(INTEGER, ForeignKey('courses.id'))

    def __init__(self, tutor_id, course_id):
        self.tutor_id = tutor_id
        self.course_id = course_id