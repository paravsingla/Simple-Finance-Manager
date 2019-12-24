from . import main
from .. import db

@auth.route('/login')
def login():
    retun 'Login'

@auth.route('/signup')
def signup():
    return 'Signup'

@auth.route('/logout')
def logout():
    return 'Logout'
