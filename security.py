from werkzeug.security import safe_str_cmp
from models.user import User


def authenticate(username, password):
    """
    Devuelve un usuario si corrobora que coincide con alguno precargado, recibe
    username y password por json
    """
    user = User.return_users_logged(username)
    if user and safe_str_cmp(user.password, password):
        return user

def identity(payload):
    """
    Recibe un id en payload que corrobora con la base de datos si coincide.
    """
    user_id = payload['identity']
    return User.return_users_id(user_id)
