from . import mongo, bcrypt
from ..codes import UserCodes


def get_user(user_id):
    user = mongo.db.users.find_one({'_id': user_id})
    if user is None:
        return UserCodes.USER_NOT_FOUND, None
    else:
        return UserCodes.USER_EXISTS, user


def add_user(user_id):
    pass


def get_all_users(user_id):
    pass


def upsert_user(user_id):
    pass
