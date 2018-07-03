from flask import current_app

from .models import *
from .ttags import generate_template_tags


class FlaskWP(object):
    def __init__(self, flask_sqlalchemy, app=None):
        self._post_class = None
        self.app = app
        self.db = flask_sqlalchemy
        self.init_tables()
        self.init_jinja_env()

        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        app.jinja_env.filters.update(generate_template_tags(self))
        # current_app.config['SQLALCHEMY_BINDS']['wordpress']

    def init_tables(self):
        self.User = generate_user_class(self.db)
        self.Post = generate_post_class(self.db)
        self.Comment = generate_comment_class(self.db)

    def init_jinja_env(self):
        self.app.jinja_env.filters.update(generate_template_tags(self))