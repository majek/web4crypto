import mybottle
import bottle
import random
import string
import hashlib
import struct

import myconfig
config = myconfig.load('exercise9')

WORDS = 4

corpus = [
    "the", "be", "to", "of", "and", "a", "in", "that", "have", "i", "it",
    "for", "not", "on", "with", "he", "as", "you", "do", "at", "this", "but",
    "his", "by", "from", "they", "we", "say", "her", "she", "or", "an", "will",
    "my", "one", "all", "would", "there", "their", "what", "so", "up", "out",
    "if", "about", "who", "get", "which", "go", "me", "when", "make", "can",
    "like", "time", "no", "just", "him", "know", "take", "person", "into",
    "year", "your", "good", "some", "could", "them", "see", "other", "than",
    "then", "now", "look", "only", "come", "its", "over", "think", "also",
    "back", "after", "use", "two", "how", "our", "work", "first", "well",
    "way", "even", "new", "want", "because", "any", "these", "give", "day",
    "most", "us"]



with open('/dev/urandom', 'rb') as f:
    seed, = struct.unpack('Q', f.read(8))
random.seed(config.get('seed', None) or seed)

secret = ''.join(random.choice(corpus)
                 for _ in range(WORDS))
secret_hash = hashlib.md5(secret.encode('ascii')).hexdigest()

print("[ ] Exercise9 secret: %r" % (secret,))


app = mybottle.Bottle()

@app.get('/', template='exercise9.html')
def login_form():
    return {'secret_hash': secret_hash, 'words':WORDS}


@app.post('/')
def login_submit():
    result = bottle.request.forms.get('password')
    if result and result == secret:
        return "The value is CORRECT! Well done! " \
               "Your reward, the secret token #9: %r (save it!)" % (config['token'],)
    else:
        bottle.abort(401, '''Nope, incorrect; try again.''')
