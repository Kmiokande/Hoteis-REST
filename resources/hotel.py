from flask_restful import Resource

hoteis = [
    {'idHotel': 'ocean',
     'name': 'Ocean House Hotel',
     'stars': 4.5,
     'cost': 80.00,
     'city': 'Santa Monica'},
    {'idHotel': 'regente',
     'name': 'Regente Hotel',
     'stars': 4.8,
     'cost': 120.00,
     'city': 'New Orleans'}
]


class Hotel(Resource):
    def get(self, idHotel):
        for hotel in hoteis:
            if hotel['idHotel'] == idHotel:
                return hotel
        return {'message': 'Hotel not found!'}, 404

    def post(self, idHotel):
        pass

    def put(self):
        pass

    def delete(self):
        pass


class Hoteis(Resource):
    def get(self):
        return {'hoteis': hoteis}
