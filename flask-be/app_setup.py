#from flask import Flask, jsonify, request, abort
import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from config import DevConfig

#app = Flask(__name__)
connex_app = connexion.App(__name__, specification_dir='./')   # circular import problem, module mentioned in api path is imported at this line
connex_app.add_api('swagger.yml')
app = connex_app.app
app.config.from_object(DevConfig)
CORS(app)

db = SQLAlchemy(app)