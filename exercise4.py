import string
import time
import random
import bottle
import mybottle

import myconfig
config = myconfig.load('exercise4')

N = 1023
K = 50
SAVED_ITEMS_LIMIT = K * (N / 10) # at most 10% of buckets full


saved_items = 0
hash_table = [[] for i in range(N)]

def hash_table_last(s):
    h = abs(s.__hash__())
    bucket = hash_table[h % N]
    if len(bucket) < 1:
        return None
    else:
        return bucket[-1]

def hash_table_add(s):
    global saved_items
    h = abs(s.__hash__())
    bucket = hash_table[h % N]
    if s in bucket:
        return True, False
    if len(bucket) >= K:
        return False, False
    bucket.append( s )
    saved_items += 1
    return True, len(bucket) == K

def hash_table_clean():
    global saved_items
    saved_items = 0
    for b in range(N):
        hash_table[b] = []


app = mybottle.Bottle()

@app.route('/', template='exercise4.html')
def login_form():
    return {'N':N }

@app.post('/')
def login_submit():
    s = bottle.request.forms.get('string')[:64]
    s.replace('<', '').replace('>','')
    #print("s=%r b=%i" % (s, abs(s.__hash__()) % N))
    added, bucket_full = hash_table_add(s)
    if added:
        if saved_items > SAVED_ITEMS_LIMIT:
            hash_table_clean()
        if not bucket_full:
            return '''Nom, nom, nom.... String memorized!'''
        else:
            return bottle.abort(500, "CRASH! Hash table buffer too long! " \
                                    "Last item in the buffer: %r " \
                                    "Your reward, the secret token #4: %r (save it!)" % (
                    hash_table_last(s), config['token']))

    else:
        return bottle.abort(500, "CRASH! Hash table buffer too long! " \
                                "Last item in the buffer: %s" \
                                "No reward this time." % (
                hash_table_last(s),))
