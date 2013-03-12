import mybottle
import bottle
import struct

import myconfig
config = myconfig.load('exercise2')


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
secret = gen.__next__()
x1 = gen.__next__()

print("[ ] Exercise2 secret: %r" % (secret,))


app = mybottle.Bottle()

@app.get('/', template='exercise2.html')
def login_form():
    return {'x1': x1}

@app.post('/')
def login_submit():
    password = bottle.request.forms.get('password')
    if password and password == str(secret):
        return "Your predition is CORRECT! LCG are indeed reversible. " \
               "Your reward, the secret token #2: %r (save it!)" % (config['token'],)
    else:
        bottle.abort(401, '''The value was incorrect; try again.''')


if __name__ == "__main__":
    PORT = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=PORT, debug=True)
