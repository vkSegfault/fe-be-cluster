### controller from MVC ###

import connexion
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from sqlalchemy_utils import database_exists
from sqlalchemy import create_engine, inspect, MetaData
from sqlalchemy.ext.declarative import declarative_base
from flask_cors import CORS
from . import config

db = SQLAlchemy()

#connex_app = connexion.App(__name__, specification_dir='./')   # circular import problem, module mentioned in api path is imported at this line
#connex_app.add_api('swagger.yml')
#app = connex_app.app

app = Flask(__name__, template_folder='../templates', static_folder='../static')
app.config.from_object(config.DevConfig)

db.init_app(app)

CORS(app)
bcrypt = Bcrypt(app)

from .api_view import view
from .api_auth import auth
from .api_base import api
app.register_blueprint(view, url_prefix='/')
app.register_blueprint(auth, url_prefix='/auth/')
app.register_blueprint(api, url_prefix='/api')

from .model import User, Note

login_manager = LoginManager()
login_manager.login_view = 'auth.login'   # if not logged in forward all Unauthorized there: auth is a bluprint object name, login is func in this file
login_manager.login_message_category = 'info'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(id):
    user = User.query.filter_by(id=int(id)).first()
    # user = User.query.get(int(id))   # equivalnet to above
    print(user)
    return user


#####################

def is_db_running(url):
    print(f"Checking if DB is running: {url}")
    assert database_exists(url)
    print(f"DB is running")

def get_db_engine():
    url = config.DevConfig.SQLALCHEMY_DATABASE_URI
    is_db_running(url)
    #engine = create_engine(url, pool_size=50, echo=True)

def create_tables():
    """Must be called within `with app.app_context():`"""
    # creates all tables defined in models.py inside connected DB
    db.create_all()

def drop_tables():
    """Must be called within `with app.app_context():`"""
    db.drop_all()

def add_user(name: str, password: str,  money: int):
    from .model import User
    if not User.query.filter_by(name=name).first():   # if there is no such user
        user = User(name=str(name), password=str(password), money=money)
        user.add()
    else:
        print("User exists... skipping")

def get_tables():
    url = config.DevConfig.SQLALCHEMY_DATABASE_URI
    engine = create_engine(url)
    inspector = inspect(engine)
    tables = inspector.get_table_names()
    return tables

def drop_table(table_name: str):
    url = config.DevConfig.SQLALCHEMY_DATABASE_URI
    engine = create_engine(url)
    base = declarative_base()
    metadata = MetaData()
    metadata.reflect(bind=engine)
    try:
        table = metadata.tables[table_name]
    except KeyError as e:
        print(f"No Table named: {table_name}")
        return None
    if table is not None:
        base.metadata.drop_all(engine, [table], checkfirst=True)

def update(name: str, money: int):
    url = config.DevConfig.SQLALCHEMY_DATABASE_URI
    engine = create_engine(url)
    base = declarative_base()
    metadata = MetaData()
    metadata.reflect(bind=engine)

    #user.update(name, money)

def exist():
    from .model import User
