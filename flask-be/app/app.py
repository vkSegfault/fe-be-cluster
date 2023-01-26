### controller from MVC ###

import connexion
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import database_exists
from sqlalchemy import create_engine, inspect
from flask_cors import CORS
from . import config

db = SQLAlchemy()

def create_app():
    #connex_app = connexion.App(__name__, specification_dir='./')   # circular import problem, module mentioned in api path is imported at this line
    #connex_app.add_api('swagger.yml')
    #app = connex_app.app
    
    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    app.config.from_object(config.DevConfig)

    db.init_app(app)
    
    CORS(app)

    from .view import view
    from .auth import auth
    from .api import api
    app.register_blueprint(view, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/auth/')
    app.register_blueprint(api, url_prefix='/api')

    from .model import User, Note

    return app

def is_db_running(url):
    print(f"Checking if DB is running: {url}")
    assert database_exists(url)
    print(f"DB is running")

def get_db_engine():
    url = config.DevConfig.SQLALCHEMY_DATABASE_URI
    is_db_running(url)
    #engine = create_engine(url, pool_size=50, echo=True)

def create_tables():
    db.create_all()

def add_user():
    from . import model
    user = model.User('Janusz', 520)
    user.add()

def get_tables():
    url = config.DevConfig.SQLALCHEMY_DATABASE_URI
    engine = create_engine(url)
    