from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt


mongo = PyMongo()
bcrypt = Bcrypt()


def user_exists(user_id, password=None):
    user = mongo.db.users.find_one({'_id': user_id})
    if password is not None and user is not None:
        hashed_password = user['password']
        return bcrypt.check_password_hash(hashed_password, password)

    return user is None


def add_user(user_id, password):
    if user_exists(user_id):
        raise ValueError("User {} already exists".format(user_id))

    hashed_pw = bcrypt.generate_password_hash(password)
    mongo.db.users.insert(
        {'_id': user_id, 'password_hash': hashed_pw, 'trials': []}
    )


def get_trial_data(user_id, trial_id):
    trial = mongo.db.users.find_one(
        {'_id': user_id, 
         'trials': {'$in': trial_id}
        }
    )

    if trial is None:
        raise ValueError(
            "No trial found for user id {} and trial id {}".format(
                user_id, trial_id
            )
        )

    return trial


def add_trial_data(user_id, trial_id, trial_data):
    user = mongo.db.users.find_one({'_id': user_id})

    if user is None:
        mongo.db.users.insert(
            {'_id': user_id,
             'trials': [{trial_id: trial_data}]
            }
        )
    else:
        trial = mongo.db.users.find_one(
            {'_id': user_id, 'trials': {'$in': trial_id}}
        )
        if trial is None:
            mongo.db.users.


def delete_trial_data(user_id, trial_id):
    raise NotImplementedError


def get_all_trials_for_user(user_id):
    raise NotImplementedError

__all__ = (
    'get_trial_data', 'set_trial_data', 'delete_trial_data', 
    'get_all_trials_for_user', 'mongo'
)
