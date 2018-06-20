__all__ = (
    "db", "cache"
)

from flask_sqlalchemy import SQLAlchemy
from flask_caching import Cache

db = SQLAlchemy()
cache = Cache(config={'CACHE_TYPE': 'simple'})