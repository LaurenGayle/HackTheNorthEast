"""
Module to read data from database 
"""

import app.views as views

from geoip import geolite2
import logging as log

from tinydb import TinyDB, Query


db = TinyDB('db.json')
log.basicConfig(filename='example.log', level=log.DEBUG)


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


def getAnger(slider6data):
    return slider6data
