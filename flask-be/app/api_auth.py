"""view for authorization"""

from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from .view_forms import RegisterForm, LoginForm
from .model import User

auth = Blueprint("auth", __name__)

@auth.route('/register', methods=['GET', 'POST'])
def register():
    # take data from HTML forms filled by user
    # sign-up functionality like validation if user already exists
    # don't write everything here, just use login functions from controller
    form = RegisterForm()

    # legit way using Web Forms
    if form.validate_on_submit():   # validate on submit checks if User clicked the button
        # POST mothod should be allowed in this route
        username = form.username.data   # field_name.data from our child Form class and .data is how we fetch data from html submit field
        print(username)
        print(f'Data from POST: {username}')
        # add this user to DB
        # return redirect( url_for('view.home') )
        return render_template( 'register.html', form=form, data=username )
    else:
        print("WebForm validation failed")
        if form.errors != {}:
            for err_msg in form.errors.values():
                print(f'Validation error: {err_msg}')
    
    # alternative, more basic approach
    # if request.method == 'POST':
    #     username = request.form['title']
    #     print(username)
    #     return redirect( url_for('view.home') )
    return render_template("register.html", form=form)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print('OnSubmit validation passed')
        # query user from db based on provided username
        user = User.query.filter_by(name=form.username.data).first()
        print(f'User is {user}')
        if user and user.verify_password(form.password.data):
            print('User exists and password matches')
            login_user(user)   # just let login manager know that current user is logged in
            flash(f"Successfuly logged in as {user.name}", category='success')
            flash("Redirecting...")
            #return render_template( 'login.html', form=form, msg=f"Successfuly logged in as {user.name}")
            return redirect(url_for('api.subpage'))   # redirection effects in not displayed flash messages
        else:
            print('Wrong password or user doesn\'t exists')
            flash(f"Wrong password or user doesn\'t exists", category='danger')
    return render_template("login.html", form=form)

@auth.route('/logout')
@login_required   # we need to be logged in to actually access this endpoint
def logout():
    logout_user()
    return redirect( url_for('view.home') )