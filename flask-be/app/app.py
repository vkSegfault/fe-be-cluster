### controller from MVC ###

import connexion
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from sqlalchemy_utils import database_exists
from sqlalchemy import create_engine, inspect, MetaData
from sqlalchemy.ext.declarative import declarative_base
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

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'   # if not logged forward there: auth is a file, login is func in this file
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return db.Query.get(int(id))

    return app

def is_db_running(url):
    print(f"Checking if DB is running: {url}")
    assert database_exists(url)
    print(f"DB is running")

def get_db_engine():
    url = config.DevConfig.SQLALCHEMY_DATABASE_URI
    is_db_running(url)
    #engine = create_engine(url, pool_size=50, echo=True)

def create_db():
    """Must be called withing `with app.app_context():`"""
    # creates db with all tables defined in models.py
    db.create_all()

def add_user(name: str, money: int):
    from . import model
    user = model.User(str(name), money)
    user.add()

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
    table = metadata.tables[table_name]
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
