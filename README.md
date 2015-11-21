[![Build passed](https://travis-ci.org/Dannnno/TextScrollServer.svg?branch=master)](https://travis-ci.org/hmc-simplification/TextScrollServer)
[![Coverage Status](https://coveralls.io/repos/Dannnno/TextScrollServer/badge.png)](https://coveralls.io/r/Dannnno/TextScrollServer)

# TextScrollServer

The backend server for the TextScroll application.



### How to get up and running for development

Start a virtual environment

```
$ pip install virtualenv
$ virtualenv TextScroll --no-site-packages
$ .\TextScroll\Scripts\activate
```

Install dependencies

```
(TextScroll) $ pip install -r requirements.txt
```

Install [MongoDB][https://www.mongodb.org/downloads].

Develop on a feature branch

```
(TextScroll) $ git branch feature/feature_name
```

Commit and push your changes.  Check the build and coverage status on Travis
and Coveralls

When ready, open a Pull Request.