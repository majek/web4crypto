import mybottle
import os

import exercise0
import exercise1
import exercise2
import exercise3
import exercise4
import exercise5
import exercise6
import exercise7
import exercise8


app = mybottle.Bottle()
app.mount('/exercise0/', exercise0.app)
app.mount('/exercise1/', exercise1.app)
app.mount('/exercise2/', exercise2.app)
app.mount('/exercise3/', exercise3.app)
app.mount('/exercise4/', exercise4.app)
app.mount('/exercise5/', exercise5.app)
app.mount('/exercise6/', exercise6.app)
app.mount('/exercise7/', exercise7.app)
app.mount('/exercise8/', exercise8.app)


@app.route('/', template='index.html')
def contact():
    return {}

if __name__ == "__main__":
    PORT = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=PORT)
