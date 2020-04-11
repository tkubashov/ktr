from flask import Flask, session

from checker import check_logged_in
app = Flask(__name__)

@app.route('/hello')
def hello():
    return 'Hello'

@app.route('/page1')
@check_logged_in
def page1():
    return 'This is page 1'

@app.route('/page2')
@check_logged_in
def page2():
    return 'This is page 2'

@app.route('/login')
def do_login():
    session['logged_in'] = True
    return  'You are now logged in'

@app.route('/logout')
def do_logout():
    session.pop('logged_in')
    return  'You are now logged out'

app.secret_key = 'SecretKey'

if __name__ == '__main__':
    app.run(debug=True)