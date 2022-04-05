from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import config


""" Globally acessible Libraries """
db = SQLAlchemy()
migrate = Migrate()

def init_app(config_name):
    """ Initializate the core application"""
    app = Flask(__name__)
    
    """ Setting up the Configuration """
    app.config.from_object(config[config_name])

    """ Initialize Plugins """
    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        """ Including our Routes """
        from . import routes, models

        return app