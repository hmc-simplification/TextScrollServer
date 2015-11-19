import importlib

from flask import Flask
from flask_restful import Api

import apis
from database import mongo


app = Flask(__name__)
api = Api(app)


def register_api_endpoints():
    """Registers the API endpoints for all different API versions,
    and prepends their URLs with the appropriate version name.
    """

    for version_name in apis.versions:
        version = importlib.import_module(
            ".apis.{}".format(version_name), 'server'
        )
        for resource, endpoint in version.endpoints:
            api.add_resource(resource, "/{}/{}".format(version_name, endpoint))


register_api_endpoints()
mongo.init_app(app)


@app.route("/")
def index():
    return "<h1>Hello, world!</h1>"
