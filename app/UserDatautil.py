"""
Module to read data from database 
"""
#TODO: ADD json decoding and read direct json value from file 
#TODO: simple add data from other user inputs to generae new data for live chart

import app.views as views
#import app.models as models
#from app.models import User
import logging as log
#import app.util as util
#from app.data import db,Database
import yaml
log.basicConfig(filename='example.log',level=log.DEBUG)


def getUserIntput(slider1data, slider2data, slider3data, slider4data, slider5data, slider6data):
    log.info("Sliders 1\n"+slider1data)
    log.info("Sliders 2\n"+slider2data)
    log.info("Sliders 3\n"+slider3data)
    log.info("Sliders 4\n"+slider4data)
    log.info("Sliders 5\n"+slider5data)
    log.info("Sliders 6\n"+slider6data)
    
    



