from flask_restful import Resource, reqparse

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
	arguments = reqparse.RequestParser()
	arguments.add_argument('name')
	arguments.add_argument('stars')
	arguments.add_argument('cost')
	arguments.add_argument('city')

	def findHotel(self, idHotel):
		for hotel in hoteis:
			if hotel['idHotel'] == idHotel:
				return hotel
		return None

	def get(self, idHotel):
		hotel = self.findHotel(idHotel)
		if hotel:
			return hotel
		return {'message': 'Hotel not found!'}, 404

	def post(self, idHotel):
		data = self.arguments.parse_args()
		newHotel = { 'idHotel': idHotel, **data }
		hoteis.append(newHotel)
		return newHotel, 200

	def put(self, idHotel):
		data = self.arguments.parse_args()
		newHotel = { 'idHotel': idHotel, **data }

		hotel = self.findHotel(idHotel)
		if hotel:
			hotel.update(newHotel)
			return newHotel, 200
		return {'message': 'Hotel not found!'}, 404

	def delete(self, idHotel):
		global hoteis
		hoteis = [hotel for hotel in hoteis if hotel['idHotel'] != idHotel]
		return {'message': 'Hotel deleted.'}


class Hoteis(Resource):
	def get(self):
		return {'hoteis': hoteis}
