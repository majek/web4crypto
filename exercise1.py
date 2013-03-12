import mybottle
import bottle
import struct

import myconfig
config = myconfig.load('exercise1')


def _lcg(state):
    return (1103515245*state + 12345) % (2**31)

def lcg_generator(seed):
    state = seed
    while True:
        state = _lcg(state)
        yield state

with open('/dev/urandom', 'rb') as f:
    seed, = struct.unpack('I', f.read(4))

gen = lcg_generator(config.get('seed', None) or seed)
x0 = gen.__next__()
secret = gen.__next__()

print("[ ] Exercise1 secret: %r" % (secret,))


app = mybottle.Bottle()

@app.get('/', template='exercise1.html')
def login_form():
    return {'x0': x0}

@app.post('/')
def login_submit():
    password = bottle.request.forms.get('password')
    if password and int(password) == secret:
        return "Your predition is CORRECT! Maybe LCG are not that good. " \
               "Your reward, the secret token #1: %r (save it!)" % (config['token'],)
    else:
        bottle.abort(401, '''Your prediction was incorrect; try again.''')


if __name__ == "__main__":
    PORT = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=PORT, debug=True)
