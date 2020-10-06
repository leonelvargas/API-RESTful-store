from flask_restful import Resource
from flask_jwt import jwt_required
from models.store import StoreModel
from models.item import ItemModel


class Store(Resource):
   
    @jwt_required()
    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json(), 200
        return {'message': f'the store {name} was not founded'}, 404  # 200= leido correctamente, 404 componente no encontrado
        
    @jwt_required()
    def post(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return {'message': f'the Store: {name} already exist'}, 400
        else:
            store = StoreModel(name) 
            store.save_to_db()
        return store.json(), 201 #creado correctamente

    @jwt_required()
    def delete(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            store.delete()
            return {'message': f'The store {name} and its items were eliminated'}
        return {'message': f'The store {name} was not find'}


class StoreList(Resource):
    @jwt_required()
    def get(self):
        return [store.json() for store in StoreModel.query.all()], 200 # or Non pythonic list(map(lambda x: x.json(), StoreModel.query.all()))
