import mybottle
import os

import exercise1
import exercise2
import exercise3
import exercise4
import exercise5


app = mybottle.Bottle()
app.mount('/exercise1/', exercise1.app)
app.mount('/exercise2/', exercise2.app)
app.mount('/exercise3/', exercise3.app)
app.mount('/exercise4/', exercise4.app)
app.mount('/exercise5/', exercise5.app)

@app.route('/', template='index.html')
def contact():
    return {}

if __name__ == "__main__":
    PORT = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=PORT)
