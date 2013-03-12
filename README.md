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

    # amend config.yaml
    $ heroku create
    $ git push heroku master

