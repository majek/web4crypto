import string
import time
import random
import bottle

import yaml

with open('config.yaml') as f:
    config = yaml.load(f.read())['exercise3']


SECRET_LEN = 12

secret_time = config.get('secret_time', None) or time.time()

# This is the default seed for systems without _urandom
random.seed(int(secret_time * 256))

secret = ''.join(random.choice(string.ascii_letters) for i in range(SECRET_LEN))
print("[ ] Exercise3 secret: %r  time: %r" % (secret, secret_time))


app = bottle.Bottle()

@app.get('/', template='exercise3.html')
def login_form():
    return {'secret_len': SECRET_LEN,
            'secret_delta_time': int(time.time() - secret_time)}

@app.post('/')
def login_submit():
    password = bottle.request.forms.get('password')
    if password == secret:
        return "Your password was CORRECT! How's that possible! OMG! " \
               "Your reward, the secret token #3: %r (save it!)" % (config['token'],)
    else:
        bottle.abort(401, '''Your password was incorrect; try again.''')
