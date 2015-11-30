"""Version 1 of the API."""

from __future__ import unicode_literals, print_function, absolute_import, \
    division

from .users import User, Users


endpoints = [
    (User, "users/<string:user_id>"),
    (Users, "users")
]
