from flask import Flask, render_template, redirect, session
from wtforms import Form, StringField, TextAreaField, PasswordField, validators


app = Flask(__name__)
app.debug = True


@app.route('/')
def index():
	return render_template('home.html')

if __name__ == '__main__':
	app.secret_key = 'secret123'
	app.run()