import os
import sys
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

db = SQLAlchemy()
migrate = Migrate()

app = Flask(__name__)
base_dir = os.getcwd()
sys.path.append(base_dir)

app.config.from_pyfile(f"{base_dir}/hibike/default.cfg")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['JSON_SORT_KEYS'] = False
app.config['JSON_AS_ASCII'] = False

CORS(app, supports_credentials=True)

from hibike.models import *
db.init_app(app)
migrate.init_app(app, db)

from hibike.controllers.auth import auth_bp
from hibike.controllers.board import board_bp
app.register_blueprint(auth_bp)
app.register_blueprint(board_bp)
