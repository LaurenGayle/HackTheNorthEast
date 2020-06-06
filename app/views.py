# -*- encoding: utf-8 -*-
"""
MIT License
Copyright (c) 2019 - present AppSeed.us
"""

# Python modules
import os
import logging

# Flask modules
from flask import render_template, request, url_for, redirect, send_from_directory
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.exceptions import HTTPException, NotFound, abort
from jinja2 import TemplateNotFound

# App modules
from app import app, bc
from app.forms import LoginForm, RegisterForm

import app.UserDatautil as data

# provide login manager with load_user callback




@app.route('/', defaults={'path': 'index.html'})
@app.route('/<path>',)
def index(path):
    try:

        if not path.endswith('.html'):
            path += '.html'

        # Serve the file (if exists) from app/templates/FILE.html
        return render_template(path)

    except TemplateNotFound:
        return render_template('page-404.html'), 404

    except:
        return render_template('page-500.html'), 500

# Return sitemap


@app.route('/sitemap.xml')
def sitemap():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'sitemap.xml')


@app.route('/process', methods=['POST'])
def Data():
    slider1data = request.form.get("output")
    slider2data = request.form.get("output1")
    slider3data = request.form.get("output2")
    slider4data = request.form.get("output4")
    slider5data = request.form.get("output5")
    slider6data = request.form.get("output6")
    
    data.getUserIntput(slider1data,slider2data,slider3data,slider4data,slider5data,slider6data)
    angry =data.getAnger(slider6data)
    return angry