from flask import Flask


app = Flask(__name__, static_folder = './public', template_folder="./static")

from templates.ems.views import ems_blueprint
# register the blueprints
app.register_blueprint(ems_blueprint)