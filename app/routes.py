from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Adrian'}
    posts = [
        {
            'author': {'username': 'Adrian'},
            'body': 'Squash is getting really popular in Ukraine'
        },
        {
            'author': {'username': 'Roman'},
            'body': 'Ultimate frisbee is getting really popular in Ukraine'
        }

    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(form.username,
                                                                   form.remember_me))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign in', form=form)
