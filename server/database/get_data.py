from flask_pymongo import PyMongo


mongo = PyMongo()

def get_records(trial_id=None):
    if trial_id is not None:
        return mongo.db.trials.find_one({'_id': trial_id})
    else:
        return mongo.db.trials.find()


def add_records(trial_id, trial_data):
    inserted_id = mongo.db.trials.insert_one(
        {'_id': trial_id, 'data': trial_data}
    ).inserted_id
    return inserted_id


def remove_records(trial_id):
    deleted_count = mongo.db.users.delete_one({'_id': trial_id}).deleted_count
    return deleted_count