from typing import Dict, List, Optional, Union

from flask import jsonify, request
from flask.views import MethodView

from volunteers.database import db_model, District, Request, Street, Volunteer


class ApiDistrict(MethodView):
    def get(self, district_id: Optional[int] = None):
        if district_id is None:
            rows = District.query.all()
            data = [{'id': row.id, 'title': row.title}
                    for row in rows]
            return jsonify(data)
        else:
            district = District.query.get(district_id)
            if district:
                district = {'id': district.id,
                            'title': district.title}
            else:
                district = {}
            return jsonify(district)


class ApiRequest(MethodView):
    methods = ['POST']

    def post(self):
        data = request.json

        if data is None:
            return jsonify(), 400

        req = Request(
            district_id=int(data.get('district')),
            street_id=int(data.get('street')),
            volunteer_id=int(data.get('volunteer')),
            address=data.get('address'),
            name=data.get('name'),
            surname=data.get('surname'),
            phone=data.get('phone'),
            text=data.get('text')
        )

        db_model.session.add(req)
        try:
            db_model.session.commit()
            return jsonify({'status': 'success'})
        except:
            return jsonify(), 500


class ApiStreet(MethodView):
    @staticmethod
    def form_data(street: Street) -> Dict[str, Union[int, str, List[int]]]:
        street = {
            'id':          street.id,
            'title':       street.title,
            'volunteers':  [volunteer.id for volunteer in street.volunteers]
        }

        return street

    def get(self, street_id: Optional[int] = None):
        if street_id is None:
            district_id = request.args.get('district')
            if district_id:
                district = District.query.get(district_id)
                if district:
                    streets = district.streets
                else:
                    return jsonify()
            else:
                streets = Street.query.all()
            data = [self.form_data(street) for street in streets]
            return jsonify(data)
        else:
            street = Street.query.get(street_id)
            street = self.form_data(street)
            return jsonify(street)


class ApiVolunteer(MethodView):
    @staticmethod
    def form_data(volunteer: Volunteer) -> Dict[str,
                                                Union[int, str, List[int]]]:
        volunteer = {
            'id':       volunteer.id,
            'name':     volunteer.name,
            'userpic':  volunteer.userpic_url,
            'phone':    volunteer.phone
        }

        return volunteer

    def get(self, volunteer_id: Optional[int] = None):
        if volunteer_id is None:
            street_id = request.args.get('streets')
            if street_id:
                street = Street.query.get(street_id)
                if street:
                    volunteers = street.volunteers
                else:
                    return jsonify()
            else:
                volunteers = Volunteer.query.all()
            data = [self.form_data(volunteer) for volunteer in volunteers]
            return jsonify(data)
        else:
            volunteer = Volunteer.query.get(volunteer_id)
            volunteer = self.form_data(volunteer)
            return jsonify(volunteer)
