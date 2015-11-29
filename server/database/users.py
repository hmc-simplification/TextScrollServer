"""Database operations for users."""

from . import mongo, bcrypt
from ..codes import UserCodes


def get_user(user_id):
    """Get a user with id `user_id`.

    Parameters
    ----------
    user_id : string
        The id of the user.

    Returns
    -------
    UserCodes
        Return code (int) for the status of the operation.  Can either
        be that the user was not found, or that the user exists.
    """

    user = mongo.db.users.find_one({'_id': user_id})
    if user is None:
        return UserCodes.USER_NOT_FOUND, None
    else:
        return UserCodes.USER_EXISTS, user


def add_user(user_id, **kwargs):
    """Add a user with id `user_id`.

    Parameters
    ----------
    user_id : string
        The id of the user to be added.
    kwargs : dict
        Other information about the user that should be logged.
    """

    pass


def get_all_users():
    """Get all users."""

    pass


def upsert_user(user_id):
    """Update an existing user, or create a new one.

    Parameters
    ----------
    user_id : str
        The id of the user to be upserted into.
    """

    pass
