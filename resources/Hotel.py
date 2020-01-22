from flask_restful import Resource

hoteis = [
    {'_id': 1,
     'name': 'Ocean House Hotel',
     'stars': 4.5,
     'cost': 80.00,
     'city': 'Santa Monica'},
    {'_id': 2,
     'name': 'Regente Hotel',
     'stars': 4.8,
     'cost': 120.00,
     'city': 'New Orleans'}
]


class Hoteis(Resource):
    def get(self):
        return {'hoteis': hoteis}
