### view from MVC ###

from flask import Blueprint, render_template

view = Blueprint('view', __name__)

@view.route('/', methods=['GET'])
def home():
    #return "<h1>Homepage</h1>", 200
    return render_template("home.html")