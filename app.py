#!/usr/bin/env python3

import bottle
import os

import timed_pw

app = bottle.Bottle()
app.mount('/exercise3', timed_pw.app)

@app.route('/', template='index')
def contact():
    return {}


if __name__ == "__main__":
    PORT = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=PORT)
