"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from FlaskWebProject import app

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    themes = ['TTM4137', 'TTM4222', 'TTM4222', 'TTM4222', 'TTM4222', 'TTM4222', 'TTM4222', 'TTM4222', 'TTM4222', 'TTM4222']
    return render_template(
        'index.html',
        title='Multiple Choice',
        year=datetime.now().year,
        themes=themes
    )

@app.route('/<theme>')
def questions(theme):
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )
