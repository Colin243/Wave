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
    user = relationship("User", back_populates = "tweets")
    tags = relationship("Tag", secondary="tweettags", back_populates="tweets")

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
    status = Column("status", TEXT, nullable=False)
    rating = Column("rating", INTEGER, nullable=False) 
    user_id = Column(INTEGER, ForeignKey('users.id'))
    user = relationship("User", back_populates = "tweets")
    tags = relationship("Tag", secondary="tweettags", back_populates="tweets")

    def __init__(self, username, name, password):
        self.name = name
        self.password = password
        self.username = username


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