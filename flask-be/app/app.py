### controller from MVC ###

import connexion
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from . import config

def create_app():
    #connex_app = connexion.App(__name__, specification_dir='./')   # circular import problem, module mentioned in api path is imported at this line
    #connex_app.add_api('swagger.yml')
    #app = connex_app.app
    
    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    app.config.from_object(config.DevConfig)
    
    CORS(app)

    from .view import view
    from .auth import auth
    from .api import api
    app.register_blueprint(view, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/auth/')
    app.register_blueprint(api, url_prefix='/api')

    return app