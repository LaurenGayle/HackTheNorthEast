"""
Module to read data from database 
"""

import app.views as views
import app.models as models
from app.models import User
import logging as log
import app.util as util
from app.data import db,Database
from flask_sqlalchemy import SQLAlchemy as db
from sqlalchemy.engine import create_engine
from sqlalchemy.orm.session import sessionmaker

from tinydb import TinyDB, Query


db = TinyDB('db.json')
log.basicConfig(filename='example.log', level=log.DEBUG)

def create_session(config):
    engine = create_engine(config['DATABASE_URI'])
    Session = sessionmaker(bind=engine)
    session = Session()
    session._model_changes = {}
    return session 

def getUser(username):

    log.debug(username)
    return username


def getId(user_id):
    log.debug("test for user id")

    log.debug(id)
    return int(user_id)


def getAge():
    return


def getUserIntput(slider1data, slider2data, slider3data, slider4data, slider5data, slider6data):
    log.info("Sliders 1\n"+slider1data)
    log.info("Sliders 2\n"+slider2data)
    log.info("Sliders 3\n"+slider3data)
    log.info("Sliders 4\n"+slider4data)
    log.info("Sliders 5\n"+slider5data)
    log.info("Sliders 6\n"+slider6data)
    
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

