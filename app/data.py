from sqlalchemy import Column, Integer, String
from . import db

class Database(db.Model):
    __tablename__ = 'emotions'

    id = db.Column(db.Integer,     primary_key=True)
    anger = db.Column(db.Integer,  unique=True)
    happy = db.Column(db.Integer,  unique=True)
    calm = db.Column(db.Integer, unique=True)
    optimistic = db.Column(db.Integer, unique=True)
    anxious = db.Column(Integer, unique=True)
    sad = db.Column(db.Integer, unique=True)
    stressed = db.Column(db.Integer, unique=True)

    def __repr__(self, anger, happy, calm, optimistic, anxious, stressed, sad):
        self.anger = anger
        self.happy = happy
        self.calm = calm
        self.optimistic = optimistic
        self.anxious = anxious
        self.sad = sad
        self.stressed = stressed
        self.anxious = anxious
        return '<emotions {}>'.format(self.id,self.anger,self.happy,self.calm,self.optimistic,self.anxious,self.sad,self.stressed)
