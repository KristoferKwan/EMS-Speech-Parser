from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextField, SelectMultipleField, FileField, DateTimeField,validators, SelectField, TextAreaField
from flask_wtf.file import FileField, FileAllowed, FileRequired, DataRequired
from wtforms.validators import NumberRange, InputRequired
from datetime import datetime

class EMSForm(FlaskForm):
    incident_number = IntegerField('Incident Number', [validators.required()])
    #unit_id = IntegerField('Unit ID', [validators.required()])
    incident_date = DateTimeField(label='Incident Date',validators=[validators.InputRequired()],format = "%d%b%Y %H:%M",default= None)
    incident_address = StringField('Incident Address', [validators.Length(min=1, max=100)]) 
    incident_city = StringField('Incident City', [validators.Length(min=1, max=100)]) 
    incident_state = StringField('Incident City', [validators.Length(min=1, max=100)]) 
    incident_zipcode = IntegerField('Incident Number', [validators.required()])
    incident_county = StringField('Incident County', [validators.Length(min=1, max=30)])
    incident_location_type = StringField("Incident Location Type", [validators.Length(min=1, max=100)])
    complaint_reported_by_dispatch = DateTimeField(label='Start time',validators=[validators.InputRequired()],format = "%d%b%Y %H:%M",default= datetime.utcnow)
    disposition = SelectField('Activity Category Type', validators=[DataRequired()], choices=[('Treated Transport EMS', 'Treated Transport EMS'), ('Cancelled', 'Cancelled'), ('Treated and Released', 'Treated and Released'), ('No Patient Found', 'No Patient Found'), ('No Treatment Required', 'No Treatment Required'), ('Dead at Scene', 'Dead at Scene')])
    patient_name =  StringField('Incident Address', [validators.Length(min=1, max=100)]) 