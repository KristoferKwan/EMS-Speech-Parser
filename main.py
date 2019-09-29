from flask import Flask, render_template, redirect, session, request, jsonify
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from models.form import EMSForm
#from flask_socketio import SocketIO, emit
from flask_bootstrap import Bootstrap
from speech_to_model import interpret_transcript

app = Flask(__name__)
app.debug = True
#socketio = SocketIO(app)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
	emsForm = EMSForm(request.form)
	return render_template('home.html', ems=emsForm)

# @socketio.on( 'parse ems' )
# def handle_parse_ems():
#     result = interpret_transcript() 
#     socketio.emit('my response', jsonify(result))

@app.route( '/parse_ems' )
def handle_parse_ems():
    result = interpret_transcript() 
    return jsonify(result)


if __name__ == '__main__':
	app.secret_key = 'secret123'
	app.run()