import argparse
import json
from pathlib import Path
from typing import NoReturn

from volunteers import app
from volunteers.database import db_model, District, Street, Volunteer


def main(args: argparse.Namespace) -> NoReturn:
    input_path = Path(args.input)
    if not input_path.exists():
        raise ValueError(f'Invalid input path {input_path}')

    with open(input_path, 'r') as file:
        raw_data = json.load(file)

    volunteers = {}
    for id_, volunteer in raw_data['volunteers'].items():
        id_ = int(id_)
        volunteers[id_] = Volunteer(
            id=id_,
            name=volunteer['name'],
            userpic_url=volunteer['userpic'],
            phone=volunteer['phone']
        )

    streets = {}
    for id_, street in raw_data['streets'].items():
        id_ = int(id_)
        streets[id_] = Street(
            id=id_,
            title=street['title'],
            volunteers=[volunteers[vol_id] for vol_id in street['volunteer']]
        )

    districts = {}
    for id_, district in raw_data['districts'].items():
        id_ = int(id_)
        districts[id_] = District(
            id=id_,
            title=district['title'],
            streets=[streets[street_id] for street_id in district['streets']]
        )

    with app.app_context():
        db_model.session.add_all(districts.values())
        db_model.session.add_all(streets.values())
        db_model.session.add_all(volunteers.values())
        db_model.session.commit()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i',
                        '--input',
                        required=True,
                        help=('A path to a csv file with data for filling '
                              'tables at database'))

    args = parser.parse_args()
    main(args)
