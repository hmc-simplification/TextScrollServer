from flask_pymongo import PyMongo


mongo = PyMongo()


def user_exists(user_id):
    user = mongo.db.users.find_one({'_id': user_id})

    return user is None

def add_user(user_id, password):
    if user_exists(user_id):
        raise ValueError("User {} already exists".format(user_id))

    mongo.db.users.insert({'_id': user_id, 'trials': []})




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
