import mybottle
import bottle

import myconfig
config = myconfig.load('exercise5')


def single_siphash_round(v0, v1, v2, v3):
    v0 += v1  # no need to mod 2^64 now
    v2 += v3
    v1 = (v1 << 13) | (v1 >> 51)
    v3 = (v3 << 16) | (v3 >> 48)
    v1 ^= v0
    v3 ^= v2
    v0 = (v0 << 32) | ((v0 >> 32) & 0xffffffff)
    v2 += v1
    v0 += v3
    v0 &= 0xffffffffffffffff
    v1 = (v1 << 17) | ((v1 >> 47) & 0x1ffff)
    v3 = ((v3 & 0x7ffffffffff) << 21) \
        | ((v3 >> 43) & 0x1fffff)
    v1 ^= v2
    v1 &= 0xffffffffffffffff
    v3 ^= v0
    v2 = ((v2 & 0xffffffff) << 32) \
        | ((v2 >> 32) & 0xffffffff)
    return v0, v1, v2, v3

v0 = config['v0']
v1 = config['v1']
v2 = config['v2']
v3 = config['v3']

w0, w1, w2, w3 = single_siphash_round(v0, v1, v2, v3)

print("[ ] Exercise5 secret w0: %r" % (w0,))


app = mybottle.Bottle()

@app.get('/', template='exercise5.html')
def login_form():
    return {'v0': v0, 'v1': v1, 'v2':v2, 'v3':v3}


@app.post('/')
def login_submit():
    result = bottle.request.forms.get('string')
    if result and result == str(w0):
        return "The value is CORRECT! Well done! " \
               "Your reward, the secret token #5: %r (save it!)" % (config['token'],)
    else:
        bottle.abort(401, '''Your code is incorrect; try again.''')
