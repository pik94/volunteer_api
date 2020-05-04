from flask import Flask
from flask_migrate import Migrate

from volunteers import config as cfg
from volunteers.database import db_model, get_connection_string
from volunteers.database.models import District, Street, Volunteer


app = Flask(__name__, template_folder='templates')
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = get_connection_string()
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db_model.init_app(app)

migrate = Migrate(app, db_model)
