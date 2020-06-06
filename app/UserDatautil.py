"""
Module to read data from database 
""" 
from app  import db

import app.views as views
import app.models as models
from app.models import User
from geoip import geolite2
import logging as log
from wtforms.fields.simple import BooleanField

<<<<<<< HEAD
log.basicConfig(filename='example.log',level=log.DEBUG)
=======
from tinydb import TinyDB, Query


db = TinyDB('db.json')
log.basicConfig(filename='example.log', level=log.DEBUG)

def create_session(config):
    engine = create_engine(config['DATABASE_URI'])
    Session = sessionmaker(bind=engine)
    session = Session()
    session._model_changes = {}
    return session 

>>>>>>> parent of 269a809... Merge remote-tracking branch 'origin/master'
def getUser(username):

    log.debug(username)
    return username

def getId(user_id):
    log.debug("test for user id")
    
    log.debug(id)
    return int(user_id)

def getAge():
    return

def getUserIntput():
    
<<<<<<< HEAD
     return    
=======
    db.insert({'type': 'anger', 'count': slider6data})
    db.insert({'type': 'happy', 'count': slider1data})
    db.insert({'type': 'sad', 'count': slider5data})
    db.insert({'type': 'Cal', 'count': slider1data})

    
    db.session.add(happy =slider1data,calm= slider2data,optimistic= slider3data,anxious=slider4data,sad=slider5data,anger=slider6data)
    querydata()
    
    
def querydata():
    angerlog = db.query(db.id, db.calm)
    for id in angerlog:
        log.warn("database data"+ str(id))
>>>>>>> parent of 269a809... Merge remote-tracking branch 'origin/master'
