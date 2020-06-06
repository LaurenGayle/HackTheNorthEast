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

def getUserLocation(ipaddr):
    match = geolite2.lookup(ipaddr)
    return match.subdivisions

def getUserIntput():
    
     return    
 


  