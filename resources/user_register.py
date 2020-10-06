from flask_restful import Resource, reqparse
from models.user import User


class UserRegister(Resource):
    
    parse = reqparse.RequestParser()
    parse.add_argument(
        "username",
        type= str,
        required= True,
        help= 'This cannot be'
    )
    parse.add_argument(
        "password",
        type= str,
        required= True,
        help= 'This cannot be'
    )

    
    def post(self):
        data = self.parse.parse_args()
        if User.return_users_logged(data['username']):
            return {'message': f'That user already exists'}, 400
        user = User(**data) # lo mismo que (data['username'], data['password'])
        user.save_to_db()
        return {'message': 'The user was created'}, 201


