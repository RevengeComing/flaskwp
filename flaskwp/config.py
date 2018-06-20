class BaseConfig:
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProdConfig:
    SQLALCHEMY_DATABASE_URI = ""


class DevConfig:
    SQLALCHEMY_DATABASE_URI = ""