from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_geek():
    return '<h1>Hello from Flask & Docker</h2>'

@app.route('/members/')
def members():
    res = jsonify({"members": "Adrian"})
    res.headers.add('Access-Control-Allow-Origin', '*')
    return res

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)   # , ssl_context=('crt.pem', 'key.pem')