"""view for authorization"""

from flask_login import login_required

from flask import Blueprint
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint("auth", __name__)

@auth.route('/login')
def login():
    return "<p>Login</p>"

@login_required   # we need to be logged in to actually access this endpoint
@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/sign-up')
def sign_up():
    return "<p>Sign Up</p>"