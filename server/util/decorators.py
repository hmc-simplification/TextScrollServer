from enum import Enum

AUTHENTICATION_LEVEL = Enum('AUTHENTICATION', 'NONE USER ADMIN RESEARCHER')


def requires_authentication(level):
    """Given resource requires authentication.

    Parameters
    ----------
    level : AUTHENTICATION_LEVEL
        The level of authentication required.

    Returns
    -------
    function : callable, type
        The function or class that requires authentication.
    """

    pass
