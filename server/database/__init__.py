from flask.ext.pymongo import PyMongo
from flask.ext.bcrypt import Bcrypt

from server import app


mongo = PyMongo(app)
bcrypt = Bcrypt(app)
