import os as os
import re as re


matcher = re.compile(r"^v\d+$")

basedir = os.path.dirname(os.path.abspath(__file__))

versions = tuple(
    directory
    for directory in os.listdir(basedir)
    if matcher.match(directory)
)
