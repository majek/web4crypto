import os
import yaml
import base64

def load(exercise):
    if os.path.exists('config.yaml'):
        with open('config.yaml') as f:
            return yaml.load(f.read())[exercise]
    else:
        return yaml.load(base64.decodestring(os.environ['CONFIG']))[exercise]

def dump():
    with open('config.yaml') as f:
        config = yaml.load(f.read())
    print("heroku config:add CONFIG=%s" % (base64.encodestring(config),))
