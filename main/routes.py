from flask import render_template, flash, redirect, url_for
from main import app
from main.forms import RegistrationForm, LoginForm
from main.models import User, Post


home_message = ("Did you know sharks only attack you when your wet?")

@app.route("/")
def home():
    return render_template('home.html', message=home_message)

@app.route("/sign up", methods=['GET', 'POST'])
def sign_up():
    form = RegistrationForm()
    if form.validate_on_submit():
        print(form.errors)
        flash(f'Account created for: {form.username.data}', 'success')
        return redirect(url_for('home'))
    else:
        print(form.errors)
    return render_template('sign-up.html', title='Sign Up', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('User logged in', 'success')
            return redirect(url_for('home'))
        else:
            flash('Incorrect Login. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/javascript")
def javascript():
    return render_template('javascript.html')
