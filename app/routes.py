from flask import render_template
from app import app
import random


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'miguel'}
    number = random.randint(0, 1000)
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        },
        {
            'author': {'username': 'Ипполит'},
            'body': 'Какая гадость эта ваша заливная рыба!!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts,
                           number=number)

