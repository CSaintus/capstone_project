from flask import Blueprint, render_template, redirect, flash, request
from werkzeug.security import check_password_hash
from flask_login import login_user, logout_user

from qweeack.models import User, db
from qweeack.forms import SignUpForm, LoginForm


auth = Blueprint('auth', __name__, template_folder='auth_templates')

@auth.route("/sign_up", methods=['GET', 'POST'])
def sign_up():
    sign_up_form = SignUpForm()

    if request.method == 'POST' and sign_up_form.validate_on_submit():
        first_name = sign_up_form.first_name.data
        last_name = sign_up_form.last_name.data
        email = sign_up_form.email.data
        password = sign_up_form.password.data

        print(first_name, last_name, email)

        if User.query.filter(User.email == email).first():
            flash('Email already exists', category='warning')
            return redirect('/sign_up')

        user = User(first_name=first_name, last_name=last_name, email=email, password=password)

        db.session.add(user)
        db.session.commit()

        flash('Account created successfully', category='success')
        return redirect('/sign_in')
    
    return render_template('sign_up.html', form=sign_up_form)

@auth.route("/sign_in", methods=['GET', 'POST'])
def sign_in():
    Loginform = LoginForm()

    if request.method == 'POST' and Loginform.validate_on_submit():
        email = Loginform.email.data
        password = Loginform.password.data
        print("sign_in info", email, password)

        user = User.query.filter(User.email == email).first()

        if user and check_password_hash(user.password, password):
            login_user(user)
            flash('Logged in successfully', category='success')
            return redirect('/')
        else:
            flash('Invalid email or password', category='warning')
            return redirect('/sign_in')
        
    return render_template('sign_in.html', form=Loginform)

@auth.route("/sign_out")
def sign_out():
    logout_user()
    return redirect('/')

