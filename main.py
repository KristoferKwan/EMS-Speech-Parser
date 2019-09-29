from flask import Flask, render_template, redirect, session
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.debug = True
socketio = SocketIO(app)

@app.route('/')
def index():
	return render_template('home.html')

if __name__ == '__main__':
	app.secret_key = 'secret123'
	socketio.run(app)