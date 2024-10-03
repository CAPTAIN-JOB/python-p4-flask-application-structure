#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1> Welcome To my page</h1>'


# Creating  a  dynamic Route

@app.route('/<string:username>')
def user(username):
    return f'<h1> Profile for {username}</h1>'


#export FLASK_RUN_PORT=5555


if __name__ == '__main__':
    app.run(port=5555,debug=True)
