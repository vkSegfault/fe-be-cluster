### view from MVC ###

from flask import Blueprint, request, flash, render_template
from flask_login import login_required

api = Blueprint('api', __name__)

@api.route('/people', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return "<h1>API --> GET people</h1>", 200
    if request.method == 'POST':
        data = request.get_json()
        data_from_form = request.form.get("some_value")   #we can fetch form data like so
        name = data['name']
        print(len(name))
        if len(name) < 2:
            flash("Name is suspicioulsy short, enter something longer, category='error'")
        return "This should be POST handled " + str(name)

@api.route('/subpage', methods=['GET'])
@login_required   # must be below .route() decoratot otherwise it will override it
def subpage():
    return render_template("subpage.html")