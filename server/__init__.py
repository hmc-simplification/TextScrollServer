"""Back-end server for the TextScroll application."""

from __future__ import unicode_literals, print_function, absolute_import, \
    division

import importlib

from flask import Flask
from flask.ext.restful import Api

from . import apis


app = Flask(__name__)
app.config['ERROR_404_HELP'] = False

app.config.update(
    ERROR_404_HELP=False
)

from . import database   # noqa

api = Api(app)

for version_name in apis.versions:
    version = importlib.import_module(
        ".apis.{0}".format(version_name), 'server'
    )
    for resource, endpoint in version.endpoints:
        api.add_resource(
            resource, "/api/{0}/{1}".format(version_name, endpoint)
        )
