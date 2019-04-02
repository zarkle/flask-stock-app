from . import app
from flask import render_template, redirect, url_for, abort


@app.route('/')
def home():
    """Home route controller."""
    return render_template('home.html')
