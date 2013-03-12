import os
import yaml
import base64


if not os.environ.get('CONFIG', None):
    print("[=] Config from 'config.yaml' file")
    with open('config.yaml') as f:
        config = yaml.load(f.read())
else:
    print("[=] Config from CONFIG env")
    config = yaml.load(base64.decodestring(os.environ['CONFIG'].encode('utf-8')))


def load(exercise):
    return config[exercise]


if __name__ == "__main__":
    with open('config.yaml.deployment') as f:
        data = f.read()
    print("heroku config:add CONFIG=%s" % (
            base64.encodestring(data.encode('utf-8')).decode().replace('\n', ''),))
