import importlib

from flask import Flask
from flask.ext.restful import Api

import apis


app = Flask(__name__)
app.config['ERROR_404_HELP'] = False

app.config.update(
    ERROR_404_HELP = False
)

from . import database

api = Api(app)

for version_name in apis.versions:
    version = importlib.import_module(
        ".apis.{}".format(version_name), 'server'
    )
    for resource, endpoint in version.endpoints:
        api.add_resource(resource, "/api/{}/{}".format(version_name, endpoint))
