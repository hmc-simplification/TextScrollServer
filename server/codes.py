"""Return codes used throughout the application."""

from __future__ import unicode_literals, print_function, absolute_import, \
    division

from enum import Enum


class UserCodes(Enum):
    """User-related return codes.

    The status of an operation, for example if a user exists, or if they
    were created, etc.
    """

    USER_EXISTS = 0
    USER_CREATED = 1
    USER_UPDATED = 2
    USER_UNCHANGED = 3
    USER_NOT_FOUND = 100
    USER_NOT_AUTHENTICATED = 101
    USER_INVALID = 102
