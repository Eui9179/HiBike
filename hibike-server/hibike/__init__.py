import os
import sys

from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from flask import Flask
from flask_apispec.extension import FlaskApiSpec
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
app.config.update({
    "APISPEC_SPEC": APISpec(
        title="hibike api",
        version="v1",
        openapi_version="2.0.0",
        plugins=[MarshmallowPlugin()],
    ),
    "APISPEC_SWAGGER_URL": "/docs.json",
    "APISPEC_SWAGGER_UI_URL": "/docs/"
})
CORS(app, supports_credentials=True)
docs = FlaskApiSpec(app)

from hibike.models import *
db.init_app(app)
migrate.init_app(app, db)

from hibike.controllers.auth import auth_bp
from hibike.controllers.board import board_bp
app.register_blueprint(auth_bp)
app.register_blueprint(board_bp)

docs.register_existing_resources()
# 스웨거에서 options 제거
for key, value in docs.spec._paths.items():
    docs.spec._paths[key] = {
        inner_key: inner_value for inner_key, inner_value in value.items() if inner_key != "options"
    }
