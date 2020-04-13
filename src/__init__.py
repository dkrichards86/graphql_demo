import logging
import sys

from environs import Env
from flask import Flask
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

from config import Config

env = Env()
env.read_env()

db = SQLAlchemy()
migrate = Migrate(directory="migrations")
ma = Marshmallow()


def register_blueprints(app):
    from src.api import api_bp
    from src.graphql import graphql_bp

    app.register_blueprint(api_bp)
    app.register_blueprint(graphql_bp)


def register_commands(app):
    from src.commands import seed

    app.cli.add_command(seed)


def register_logger(app):
    handler = logging.StreamHandler(sys.stdout)
    if not app.logger.handlers:
        app.logger.addHandler(handler)


def create_app(config_object=Config):
    app = Flask(__name__.split(".")[0])
    app.config.from_object(config_object)

    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)

    register_blueprints(app)
    register_commands(app)
    register_logger(app)

    return app
