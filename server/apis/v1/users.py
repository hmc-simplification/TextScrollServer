"""API for user operations."""

from __future__ import unicode_literals, print_function, absolute_import, \
    division

from flask import jsonify, make_response, request
from flask.ext.restful import Resource

from server.database.users import get_user, add_user, get_all_users, upsert_user
from server.codes import UserCodes


class Users(Resource):
    """Resource at the /users endpoint.

    Supports the GET method only.
    """

    def get(self):
        """Get json document of all users.

        Returns
        -------
        Response
            An HTTP Response that has data on all users.
        """

        try:
            return jsonify(get_all_users())
        except Exception:
            return make_response("An unknown error occurred.", 500)


class User(Resource):
    """Resource at the /users/<user_id> endpoint.

    Supports the GET, POST, and PUT methods.
    """

    def get(self, user_id):
        """Get the user `user_id`.

        Parameters
        ----------
        user_id : str
            The user's id.

        Returns
        -------
        Response
            Response from the server. It can have a 200 response if the
            user was found and a 404 if the user doesn't exist.
        """

        return_code, user_data = get_user(user_id)

        try:
            if return_code == UserCodes.USER_EXISTS:
                return jsonify(user_data)
            elif return_code == UserCodes.USER_NOT_FOUND:
                return make_response(
                    "User with id {0} could not be found".format(user_id), 404
                )
            elif return_code == UserCodes.USER_INVALID:
                return make_response("User id or password is invalid.", 400)
            elif return_code == UserCodes.USER_NOT_AUTHENTICATED:
                return make_response("Authentication Failed", 403)
            else:
                # How did this happen???
                # TODO log something in these cases
                raise Exception()
        except Exception:
            return make_response("An unknown error occurred.", 500)

    def post(self, user_id):
        """Create a new user with id `user_id`.

        Parameters
        ----------
        user_id : str
            The user's id.

        Returns
        -------
        Response
            Response from the server. 201 if the user was created, 400 if the
            user exists or was invalid.
        """

        return_code = add_user(user_id)

        try:
            if return_code == UserCodes.USER_CREATED:
                return make_response("User {0} created!".format(user_id), 201)
            elif return_code == UserCodes.USER_EXISTS:
                return make_response(
                    "User id {0} already exists.".format(user_id), 400
                )
            elif return_code == UserCodes.USER_INVALID:
                return make_response("User id or password is invalid.", 400)
            else:
                raise Exception()
        except Exception:
            return make_response("An unknown error occurred.", 500)

    def put(self, user_id):
        """Update or create a new user with id `user_id`.

        Parameters
        ----------
        user_id : str
            The user's id.

        Returns
        -------
        Response
            Response from the server. 201 if the user was created, 200 if the
            user was updated, 400 if the user was invalid.
        """

        return_code = upsert_user(user_id)

        try:
            if return_code == UserCodes.USER_CREATED:
                return make_response("User {0} created!".format(user_id), 201)
            elif return_code == UserCodes.USER_UPDATED:
                return make_response(
                    "User id {0} was updated.".format(user_id), 200
                )
            elif return_code == UserCodes.USER_UNCHANGED:
                return make_response(
                    "User id {0} was unchanged.".format(user_id), 304
                )
            elif return_code == UserCodes.USER_INVALID:
                return make_response("User id or password is invalid.", 400)
            else:
                raise Exception()
        except Exception:
            return make_response("An unknown error occurred.", 500)
