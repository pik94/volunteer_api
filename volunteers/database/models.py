from volunteers.database.database import db


streets_volunteers = db.Table(
    'streets_volunteers',
    db.Column('street_id', db.Integer, db.ForeignKey('streets.id')),
    db.Column('volunteer_id', db.Integer, db.ForeignKey('volunteers.id'))
)


districts_streets = db.Table(
    'districts_streets',
    db.Column('district_id', db.Integer, db.ForeignKey('districts.id')),
    db.Column('street_id', db.Integer, db.ForeignKey('streets.id'))
)


class District(db.Model):
    __tablename__ = 'districts'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)

    streets = db.relationship('Street', back_populates='districts',
                              secondary=districts_streets)


class Request(db.Model):
    __tablename__ = 'requests'

    id = db.Column(db.Integer, primary_key=True)
    district_id = db.Column(db.Integer, db.ForeignKey('districts.id'))
    street_id = db.Column(db.Integer, db.ForeignKey('streets.id'))
    volunteer_id = db.Column(db.Integer, db.ForeignKey('volunteers.id'))
    address = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)
    surname = db.Column(db.String, nullable=False)
    phone = db.Column(db.String, nullable=False)
    text = db.Column(db.String, nullable=False)


class Street(db.Model):
    __tablename__ = 'streets'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)

    districts = db.relationship('District', back_populates='streets',
                                secondary=districts_streets)
    volunteers = db.relationship('Volunteer', back_populates='streets',
                                 secondary=streets_volunteers)


class Volunteer(db.Model):
    __tablename__ = 'volunteers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    userpic_url = db.Column(db.String, nullable=False)
    phone = db.Column(db.String, nullable=False)

    streets = db.relationship('Street', back_populates='volunteers',
                              secondary=streets_volunteers)
