Simple web servers for testing cryptographic tactics
----------------------------------------------------

Requirements:

 - python 3
 - virtualenv


To run:

    $ ln -s config.yaml.default config.yaml
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
