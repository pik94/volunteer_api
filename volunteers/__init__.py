from flask import Flask
from flask_migrate import Migrate

from volunteers import config as cfg
from volunteers.database import db_model, get_connection_string
from volunteers.views import ApiDistrict, ApiRequest, ApiStreet, ApiVolunteer


app = Flask(__name__, template_folder='templates')
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = get_connection_string()
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db_model.init_app(app)

migrate = Migrate(app, db_model)


api_district = ApiDistrict.as_view('districts')
app.add_url_rule('/districts', view_func=api_district)
app.add_url_rule('/districts/<int:district_id>', view_func=api_district)

api_request = ApiRequest.as_view('request')
app.add_url_rule('/request', view_func=api_request)

api_street = ApiStreet.as_view('streets')
app.add_url_rule('/streets', view_func=api_street)
app.add_url_rule('/streets/<int:street_id>', view_func=api_street)

api_volunteer = ApiVolunteer.as_view('volunteers')
app.add_url_rule('/volunteers', view_func=api_volunteer)
app.add_url_rule('/volunteers/<int:volunteers_id>', view_func=api_volunteer)
