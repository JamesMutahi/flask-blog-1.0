from flask import render_template,request,redirect,url_for,abort
from . import main

# Views
@main.route('/')
def index():

    title = 'Flask Blog'

    return render_template('index.html', title=title)

@main.route('/home')
def home():

    title = 'Home'

    return render_template('home.html', title=title)