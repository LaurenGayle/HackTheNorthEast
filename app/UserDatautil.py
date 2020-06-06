"""
Module to read data from database 
"""
from app import db

import app.views as views
from app.models import User
from geoip import geolite2
import logging as log
import app.util as util




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


def getAnger(slider6data):
    return slider6data