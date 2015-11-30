"""Runs the server."""

from __future__ import unicode_literals, print_function, absolute_import, \
    division

from server import app


if __name__ == '__main__':
    app.run(debug=True)
