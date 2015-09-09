import os as _os
import re as _re


_match = _re.compile(r"^v\d+$")

_basedir = _os.path.dirname(_os.path.abspath(__file__))

versions = [
    directory
    for directory in _os.listdir(_basedir)
    if _match.match(directory)
]

__all__ = ['versions'] + versions
