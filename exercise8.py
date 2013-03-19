import mybottle
import bottle
# We don't care about seed here.
import random
import string
import hashlib

LENGTH=7
COUNT=30

def _gen_passwords(chars, length, count):
    return [''.join(random.choice(chars) for _ in range(LENGTH)).encode('ascii')
            for _ in range(count)]

def gen_unsalted(chars, length, count):
    return [hashlib.sha1(p).hexdigest() for p in _gen_passwords(chars, length, count)]

def gen_salted(chars, length, salt_length, count):
    passwords =  _gen_passwords(chars, length, count)
    salts =  _gen_passwords(chars, salt_length, count)
    return [
        '$SHA1p$%s$%s' % (salts[i].decode('ascii'),
                          hashlib.sha1(salts[i] + passwords[i]).hexdigest())
        for i in range(count)]

def gen_weakly_salted(chars, length, salt, count):
    passwords =  _gen_passwords(chars, length, count)
    return [
        '$SHA1p$%s$%s' % (salt.decode('ascii'),
                          hashlib.sha1(salt + passwords[i]).hexdigest())
        for i in range(count)]


app = mybottle.Bottle()

@app.get('/', template='exercise8.html')
def login_form():
    return {
        'unsalted': gen_unsalted(string.digits, LENGTH, COUNT),
        'salted': gen_salted(string.digits, LENGTH, 4, COUNT),
        'weakly_salted': gen_weakly_salted(string.digits, LENGTH, "aaaa".encode('ascii'), COUNT),
        'length': LENGTH,
        }
