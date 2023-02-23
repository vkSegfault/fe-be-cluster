### View from MVC ###

from flask import Blueprint, render_template, flash

view = Blueprint('view', __name__)

@view.route('/', methods=['GET'])
def home():
    #return "<h1>Homepage</h1>", 200
    flash('DUPA MAMUTA')
    return render_template("home.html", arg1="arg passed from Flask render tamplate")