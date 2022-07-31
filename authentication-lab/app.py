from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase

config = {

  "apiKey": "AIzaSyA29l6kgtyY2WVWDbioXYyZEJRQ3kdPBd4",

  "authDomain": "fir-lab1-2d744.firebaseapp.com",

  "projectId": "fir-lab1-2d744",

  "storageBucket": "fir-lab1-2d744.appspot.com",

  "messagingSenderId": "211282416884",

  "appId": "1:211282416884:web:79a6b6297f72eb2067faa1",

  "measurementId": "G-KM6F438GSW",
  "databaseURL" : ""
}

firebase=pyrebase.initialize_app(config)
auth = firebase.auth()

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'


@app.route('/', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        error=""
        email = request.form['email']
        password = request.form['password']
        try:
            login_session['user']=auth.sign_in_with_email_and_password(email,password)
            return redirect(url_for('add_tweet'))
        except:
            error="Authentication failed"
    return render_template("signin.html")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        error=""
        email = request.form['email']
        password = request.form['password']
        try:
            login_session['user']=auth.create_user_with_email_and_password(email,password)
            return redirect(url_for('add_tweet'))
        except:
            error="Authentication failed"

    return render_template("signup.html")


@app.route('/add_tweet', methods=['GET', 'POST'])
def add_tweet():
    return render_template("add_tweet.html")


if __name__ == '__main__':
    app.run(debug=True)