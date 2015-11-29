"""Version 1 of the API."""

from users import User, Users


endpoints = [
    (User, "users/<string:user_id>"),
    (Users, "users")
]
