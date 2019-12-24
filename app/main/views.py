from datetime import datetime
from flask import render_template, session, redirect, url_for
from . import main
from .. import db
from flask_login import login_required, current_user

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/dashboard')

def dashboard():
    return render_template('dashboard.html', name=current_user.name)
