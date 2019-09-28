from flask import render_template, Blueprint, jsonify
ems_blueprint = Blueprint('ems',__name__)

@ems_blueprint.route('/')
@ems_blueprint.route('/ems')
def index():
    return render_template("index.html")

@ems_blueprint.route('/parse_ems_info')
def parse_info():
    data = {
          "incident_address" : '40 Victor Dr. East North Port',
          "incident_number" : 12345,
    }
    return data.jsonify()