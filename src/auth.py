from flask import Blueprint

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return "<h1>login</h1>"

@auth.route('/logout')
def logout():
    return "<h1>logout</h1>"

@auth.route('/sign-up')
def signin():
    return "<h1>sign up</h1>"

