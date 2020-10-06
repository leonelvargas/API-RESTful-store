import os

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identity
from resources.user_register import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList


app= Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key= 'leo' #clave para descifrar la comunicacion mediante el JWT, este codifica las comunicaciones y se usa esta key para traducir luego.
api= Api(app)

    
jwt = JWT(app, authenticate, identity) 
"""
crea un endpoint /auth, llama a la funcion authenticate para generar un 
Jason Web Token especifico para el usuario, en este tiene toda la info,
del usuario. Luego, lo chequea con identity en cada llamada de jwt_required(), comparan 
los id del usuario, ya que el JWT tiene toda la info del usuario, si la llamada de alguna 
funcion corresponde el id de ese usuario con el JWT generado, se realizara la funcion 
"""

api.add_resource(Item, '/item/<string:name>/<int:store_id>') #Se crean los diferentes endpoints, este programa presenta un mismo endpoint pero con multiples HTTP verbs
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')

if __name__ == "__main__": #si el nombre de la app, corre en __main__ se ejecuta
    from db import db
    db.init_app(app)
    app.run(debug= True) #debug sirve para debugear, cuando se termina el desarrollo se tiene que cambiar
    
