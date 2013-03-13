import mybottle
import bottle
import struct

import myconfig
config = myconfig.load('exercise0')


secret = config['secret']

print("[ ] Exercise0 secret: %r" % (secret,))

app = mybottle.Bottle()

@app.get('/', template='exercise0.html')
def login_form():
    return {}

@app.post('/')
def login_submit():
    password = bottle.request.forms.get('password')
    if password and password == secret:
        return "Your guess is CORRECT! I need to find a better way to remember passwords. " \
               "Your reward, the secret token #0: %r (save it!)" % (config['token'],)
    else:
        bottle.abort(401, '''Your guess was incorrect; try again.''')
