|Build passed| |Coverage Status| |Documentation|

TextScrollServer
================

The backend server for the TextScroll application.

How to get up and running for development
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Start a virtual environment

::

    $ pip install virtualenv
    $ virtualenv TextScroll --no-site-packages
    $ .\TextScroll\Scripts\activate

2. Install dependencies

::

    (TextScroll) $ pip install -r requirements.txt

3. Install `MongoDB <https://www.mongodb.org/downloads>`__.
4. Develop on a feature branch

::

    (TextScroll) $ git branch feature/feature_name

5. Commit and push your changes.
6. Check the build and coverage status on Travis and Coveralls
7. When ready, open a Pull Request.

.. |Build passed| image:: https://travis-ci.org/hmc-simplification/TextScrollServer.svg?branch=master
   :target: https://travis-ci.org/hmc-simplification/TextScrollServer
.. |Coverage Status| image:: https://coveralls.io/repos/Dannnno/TextScrollServer/badge.png
   :target: https://coveralls.io/r/Dannnno/TextScrollServer
.. |Documentation| image:: https://readthedocs.org/projects/textscrollserver/badge/?version=latest
   :target: http://textscrollserver.readthedocs.org/en/latest/?badge=latest
