from flask import Flask

from .ext import *
from .config import ProdConfig, DevConfig

def create_app(config="dev"):
    app = Flask(__name__)

    configure(app, config)
    configure_ext(app)

    return app

def configure(app, config):
    if config == "prod":
        app.config.from_object(ProdConfig)
    elif config == "dev":
        app.config.from_object(DevConfig)        

def configure_ext(app):
    db.init_app(app)
    cache.init_app(app)