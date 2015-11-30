"""The API of the backend-server."""

from __future__ import unicode_literals, print_function, absolute_import, \
    division

import os
import re


matcher = re.compile(r"^v\d+$")

basedir = os.path.dirname(os.path.abspath(__file__))

versions = tuple(
    directory
    for directory in os.listdir(basedir)
    if matcher.match(directory)
)
