from db import db


class User(db.Model):
    """
    Creamos una clase de Usuario para tener multiples objetos de esta.
    """
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key= True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))

    def __init__(self, username, password):
        self.username= username
        self.password= password
    

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def return_users_logged(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def return_users_id(cls, _id):
        return cls.query.filter_by(id=_id).first()