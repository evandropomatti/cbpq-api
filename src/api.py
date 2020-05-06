from flask import Flask
app = Flask(__name__)

@app.route('/api/cbpq')
def cbpq():
    return 'Hello, World!'

app.run()