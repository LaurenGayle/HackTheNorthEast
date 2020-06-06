"""
Module to read data from database 
""" 

from app  import db

import app.views as views
import app.models as models
from app.models import User
import logging as log

log.basicConfig(filename='example.log',level=log.DEBUG)
def getUser(username):
    log.info("test for username")
    users = User.query.filter_by(user = username).first()
    log.debug(users)
    return users

def getId(user_id):
    log.debug("test for user id")
    
    log.debug(id)
    return int(user_id)

def getAge():
    return

def getLocation():
    return

def getUserIntput():
     return    
 
 
  