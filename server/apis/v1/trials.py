"""API for trial operations."""

from flask import jsonify, make_response, request
from flask.ext.restful import Resource

# from server.database import get_all_trials


# class Trials(Resource):

#     def get(self):
#         return jsonify(get_all_trials())


# class Trial(Resource):

#     # def get(self, user_id, trial_id):
#     #     try:
#     #         trial = get_trial_data(user_id, trial_id)
#     #         return jsonify(trial)
#     #     except ValueError:
#     #         return make_response(
#     #             ('A user {} or trial {} does not exist'.format(
#     #                 user_id, trial_id),
#     #              400,
#     #              [{}])
#     #         )

#     def post(self, user_id, trial_id):
#         trial_data = request.args.get('trial_data')
#         try:
#             add_trial_data(user_id, trial_id, trial_data)
#         except ValueError:
#             return make_response(
#                 ('A trial with this value already exists',
#                  400,
#                  [{}])
#             )
#         else:
#             return make_response(
#                 ('Trial {} data successfully submitted'.format(trial_id),
#                  201,
#                  [{}])
#             )

#     # def delete(self, user_id, trial_id):
#     #     try:
#     #         remove_trial_data(user_id, trial_id)
#     #     except ValueError:
#     #         # There is no trial for this id
#     #         return make_response(
#     #             ('A trial with this value does not exist',
#     #              400,
#     #              [{}])
#     #         )
#     #     else:
#     #         return make_response(
#     #             ('Trial {} data successfully removed'.format(trial_id),
#     #              201,
#     #              [{}])
#     #         )


# # class TrialsForUser(Resource):

# #     def get(self, user_id):
# #         return jsonify(get_all_trials_for_user(user_id))
