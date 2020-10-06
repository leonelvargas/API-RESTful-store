from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel


class Item(Resource):
    parse = reqparse.RequestParser()
    parse.add_argument(
    'price',
    type=float,
    required=True,
    help='This cannot be left blanck!')
    
    @jwt_required()
    def get(self, name, store_id):
        item = ItemModel.find_by_name(name, store_id)
        if item:
            return item.json(), 200
        return {'message': f'the item {name} was not founded'}, 404  # 200= leido correctamente, 404 componente no encontrado
        
    @jwt_required()
    def post(self, name, store_id):
        item = ItemModel.find_by_name(name, store_id)
        if item:
            return {'message': f'the Item: {name} with store_id:{store_id} already exist'}, 400
        else:
            data = self.parse.parse_args()
            item = ItemModel(name, data['price'], store_id)
            item.save_to_db()
        return item.json(), 201 #creado correctamente
 
    @jwt_required()
    def put(self, name, store_id):
        data = self.parse.parse_args()
        item = ItemModel.find_by_name(name, store_id)
        if item:
            item.price = data['price']
        else:
            item = ItemModel(name, data['price'], store_id)
        item.save_to_db()
        return item.json()

    @jwt_required()
    def delete(self, name, store_id):
        item = ItemModel.find_by_name(name, store_id)
        if item:
            item.delete()
        return {'message': f'The item {name} with store_id:{store_id} was eliminated'}


class ItemList(Resource):
    @jwt_required()
    def get(self):
        return {'items': [x.json() for x in ItemModel.query.all()]}, 200 # Non-Pythonic form --> list(map(lambda x: x.json(), ItemModel.query.all()))
        