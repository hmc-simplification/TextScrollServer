from flask import jsonify, make_response, request
from flask_restful import Resource

from server.database import get_records, add_records, remove_records


class Trial(Resource):

    def get(self, trial_id):
        try:
            return jsonify(get_records(trial_id))
        except ValueError:
            return make_response(
                ('A trial with this value does not exist',
                 400,
                 [{}])
            )

    def post(self, trial_id):
        trial_data = request.args.get('trial_data')
        try:
            add_records(trial_id, trial_data)
        except ValueError:
            # There is already a value for this trial id
            return make_response(
                ('A trial with this value already exists',
                 400,
                 [{}])
            )
        else:
            return make_response(
                ('Trial {} data successfully submitted'.format(trial_id),
                 201,
                 [{}])
            )

    def delete(self, trial_id):
        try:
            remove_records(trial_id)
        except ValueError:
            # There is no trial for this id
            return make_response(
                ('A trial with this value does not exist',
                 400,
                 [{}])
            )
        else:
            return make_response(
                ('Trial {} data successfully removed'.format(trial_id),
                 201,
                 [{}])
            )


class Trials(Resource):

    def get(self):
        return jsonify(get_records())
