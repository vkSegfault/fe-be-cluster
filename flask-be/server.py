from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)

username = 'user'
password = 'pass'
database = 'mydb'

app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{username}:{password}@localhost:5432/{database}"

db = SQLAlchemy(app)

class Users(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(1000))
    money = db.Column(db.Integer)

    def __init__(self, name, money) -> None:
        super().__init__()
        self.name = name
        self.money = money

    def __repr__(self) -> str:
        return f'ID: {self.id}'

@app.route('/', methods=['GET'])
def hello_geek():
    return '<h1>Hello from Flask & Docker</h2>'

@app.route('/members/', methods=['GET'])
def members():
    res = jsonify({"members": "Adrian"})
    res.headers.add('Access-Control-Allow-Origin', '*')
    return res

@app.route('/api/v1/users', methods=['GET'])
def read_users():
    # temp add something to DB
    # user = Users(name='Adrian', money=23)
    # db.session.add(user)
    # db.session.commit()
    # retrieve it
    users = Users.query.all()
    print(users)

@app.route('/api/v1/user', methods=['GET', 'POST'])
def add_user():
    if request.method == "POST":
        pass

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(host="127.0.0.1", port=5000, debug=True)   # , ssl_context=('crt.pem', 'key.pem')