miAppFlask
======================

    $ git clone https://github.com/afgarcia/miappflask.git

Python 3.6 with `venv`
----------------------

    $ python3.6 -m venv venv
    $ source venv/bin/activate
    $ pip install -r requirements.txt
    $ export FLASK_APP=miappflask
    $ flask create_all
    $ flask run


Python 2.7 with `virtualenv`
----------------------------

    $ virtualenv venv
    $ source venv/bin/activate
    $ pip install -r requirements.txt
    $ export FLASK_APP=app.py
    $ flask create_all
    $ flask run

