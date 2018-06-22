from flask import current_app

from .models import *
from .ttags import flask_wp_filters


class FlaskWP(object):
    def __init__(self, flask_sqlalchemy, app=None):
        self._post_class = None
        self.app = app
        self.db = flask_sqlalchemy
        self.Post = generate_post_class(self.db)

        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        app.jinja_env.filters.update(flask_wp_filters)
        # current_app.config['SQLALCHEMY_BINDS']['wordpress']