# -*- encoding: utf-8 -*-
"""
MIT License
Copyright (c) 2019 - present AppSeed.us
"""

from app         import db
from flask_login import UserMixin

class User(UserMixin, db.Model):

    id       = db.Column(db.Integer,     primary_key=True)
    anger = db.Column(db.Integer,  unique = True)
    happy = db.Column(db.Integer,  unique = True)
    calm = db.Column(db.Integer, unique = True)
    optimistic = db.Column(db.Integer, unique = True)
    anxious = db.Column(db.Integer, unique = True)
    sad = db.Column(db.Integer, unique = True)
    stressed =  db.Column(db.Integer, unique = True)
   
    
    def __init__(self, anger,happy,calm,optimistic,anxious,stressed, sad):
        self.anger       = anger
        self.happy       = happy
        self.calm       = calm 
        self.optimistic       = optimistic 
        self.anxious       = anxious
        self.sad       = sad
        self.stressed       = stressed 
        self.anxious       = anxious 
    def __repr__(self):
        return str(self.id) + ' - ' + str(self.user)

    def save(self):

        # inject self into db session    
        db.session.add ( self )

        # commit change and save the object
        db.session.commit( )

        return self 
