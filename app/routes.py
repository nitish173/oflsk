from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {
        'username': 'nitishhh'
    }
    posts = [
        {
            'author': 'nitish',
            'body': 'Lorem ipsum'
        },
        {
            'author': 'ram',
            'body': 'Lorem ipsum dolores'
        },
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)