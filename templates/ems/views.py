from flask import render_template, Blueprint
ems_blueprint = Blueprint('ems',__name__)

@ems_blueprint.route('/')
@ems_blueprint.route('/ems')
def index():
    return render_template("index.html")