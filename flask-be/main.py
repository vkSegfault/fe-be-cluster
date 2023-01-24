from app_setup import app


@app.route('/', methods=['GET'])
def hello_geek():
    return '<h1>Hello from Flask & Docker</h2>'

@app.route('/members/', methods=['GET'])
def members():
    res = jsonify({"members": "Adrian"})
    res.headers.add('Access-Control-Allow-Origin', '*')
    return res

@app.route('/health/', methods=['GET'] )
def health_check():
    # both ways allow manually returning http code
    #abort(400)
    return "Health check", 200

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
    # with app.app_context():
    #     db.create_all()
    app.run(host="127.0.0.1", port=5000, debug=True)   # , ssl_context=('crt.pem', 'key.pem')