""" Flask Configuration """

from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
print(basedir)
load_dotenv(path.join(basedir, '.env'))

class Config:
    """ Base Config """
    SECRET_KEY = environ.get('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProdConfig(Config):
    ENV = 'production'
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = environ.get('PROD_DATABASE_URL') or \
        'sqlite:///' + path.join(basedir, 'prod-app.db')

class DevConfig(Config):
    ENV = 'development'
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + path.join(basedir, 'dev-app.db')

config = {
    'development': DevConfig,
    'production' : ProdConfig
}