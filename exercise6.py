import mybottle
import bottle
import random
import string
import hashlib
import struct

import myconfig
config = myconfig.load('exercise6')

SECRET_LEN = 6


with open('/dev/urandom', 'rb') as f:
    seed, = struct.unpack('Q', f.read(8))
random.seed(seed)

chars = string.ascii_lowercase + string.digits
secret = config.get('secret', None) or ''.join(random.choice(chars)
                                           for _ in range(SECRET_LEN))
secret_hash = hashlib.md5(secret.encode('ascii')).hexdigest()

print("[ ] Exercise6 secret: %r  hash: %r" % (secret, secret_hash))


app = mybottle.Bottle()

@app.get('/', template='exercise6.html')
def login_form():
    return {'secret_hash': secret_hash, 'secret_len':SECRET_LEN}


@app.post('/')
def login_submit():
    result = bottle.request.forms.get('string')
    if result and result == secret:
        return "The value is CORRECT! Well done! " \
               "Your reward, the secret token #6: %r (save it!)" % (config['token'],)
    else:
        bottle.abort(401, '''Nope, incorrect; try again.''')
