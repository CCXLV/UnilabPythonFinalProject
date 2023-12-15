import uuid

from flask import Blueprint, request, render_template, redirect, url_for
from flask_login import login_user, logout_user

from src.models import User 
from src.views.auth.forms import LoginForm, RegisterForm


auth_blueprint = Blueprint('auth',  __name__)


@auth_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter(User.email == form.email.data).first()
        
        if user and user.check_password(form.password.data):
            login_user(user)

            next = request.args.get('next', None)
            if next:
                return redirect(next)
            
        return redirect(url_for('main.home'))

    return render_template('auth/login.html', form=form)


@auth_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        already_registered_email = User.query.filter_by(email=form.email.data).first()
        if not already_registered_email:
            user = User(user_id=str(uuid.uuid4())[:8], username=form.username.data, email=form.email.data, password=form.password.data, role_id=1)
            user.create()

            return redirect(url_for('auth.login'))
        else:
            return redirect(url_for('auth.register`'))

    return render_template('auth/register.html', form=form)


@auth_blueprint.route('/logout', methods=['GET', 'POST'])
def logout():
    logout_user()
    return redirect(url_for('main.home'))