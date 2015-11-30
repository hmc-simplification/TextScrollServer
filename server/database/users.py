"""Database operations for users."""

from __future__ import unicode_literals, print_function, absolute_import, \
    division

import functools
import re

from . import mongo, bcrypt
from ..codes import UserCodes


def validate_username(function):
    """Validate that a username meets the criteria.

    Parameters
    ----------
    function : callable
        The function that needs validation.

    Returns
    -------
    wrapper : callable
        The decorated function.

    Notes
    -----
    The wrapped function is expected to take a first argument of a
    string `user_id`, and then variable args and kwargs.  The user_id is
    expected to have between 1 and 30 characters without any whitespace
    characters.
    """

    matcher = re.compile(r'\S{1,30}')

    @functools.wraps(function)
    def wrapper(user_id, *args, **kwargs):
        if not matcher.match(user_id):
            return UserCodes.USER_INVALID
        else:
            return function(user_id, *args, **kwargs)
    return wrapper


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


@validate_username
def add_user(user_id, **kwargs):
    """Add a user with id `user_id`.

    Parameters
    ----------
    user_id : string
        The id of the user to be added.
    kwargs : dict
        Other information about the user that should be logged.
    """

    user = mongo.db.users.find_one({'_id': user_id})

    kwargs['_id'] = user_id

    if user is None:
        mongo.db.users.insert(kwargs)
        return UserCodes.USER_CREATED
    else:
        return UserCodes.USER_EXISTS


def get_all_users():
    """Get all users."""

    pass


@validate_username
def upsert_user(user_id, **kwargs):
    """Update an existing user, or create a new one.

    Parameters
    ----------
    user_id : str
        The id of the user to be upserted into.
    """

    user = mongo.db.users.find_one({'_id': user_id})

    if user is None:
        return add_user(user_id, **kwargs)
    elif kwargs:
        mongo.db.users.update({'_id': user_id}, {'$set': kwargs})
        return UserCodes.USER_UPDATED
    else:
        return UserCodes.USER_UNCHANGED
