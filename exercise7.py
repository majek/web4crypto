import mybottle
import bottle



app = mybottle.Bottle()

@app.get('/', template='exercise7.html')
def login_form():
    return {}
