### view from MVC ###

from flask import Blueprint, request, flash

api = Blueprint('api', __name__)

@api.route('/people', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return "<h1>API --> GET people</h1>", 200
    if request.method == 'POST':
        data = request.get_json()
        name = data['name']
        print(len(name))
        if len(name) < 2:
            flash("Name is suspicioulsy short, enter somehting longer, category='error'")
        return "This should be POST handled " + str(name)