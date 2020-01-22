from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

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


api.add_resource(Hoteis, '/hoteis')

if __name__ == '__main__':
    app.run(debug=True)
