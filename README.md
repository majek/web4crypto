Assignments for Pragmatic Crypto seminar:
-----

Part 1
----

Assignments 1-3:

 * https://pragmaticcrypto.herokuapp.com/exercise1/
 * https://pragmaticcrypto.herokuapp.com/exercise2/
 * https://pragmaticcrypto.herokuapp.com/exercise3/


Slides:

  * https://speakerdeck.com/majek04/pragmatic-crypto-number-1





How to run the server
-----------

Requirements:

 - python 3
 - virtualenv

To run:

    $ make
    $ . venv/bin/activate
    $ python app.py


To deploy on heroku:

    $ heroku create
    $ heroku scale web=1
    $ git push heroku master

Alternatively:

    # amend config.yaml.deployment
    $ python myconfig.py
    $ heroku config:add CONFIG=...
