from app import app
from flask import render_template


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
