from project_instance.config import *


class Config(object):
    """
       Common configurations
       """
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_precious_secret_key')
    DEBUG = False


class DevConfig(Config):
    """
       Development configurations
       """

    DEBUG = True
    SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProdConfig(Config):
    """
    Production configurations
    """

    DEBUG = False


class TestConfig(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = TEST_SQLALCHEMY_DATABASE_URI
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


app_config = {
    'dev': DevConfig,
    'test': TestConfig,
    'prod': ProdConfig
}
key = Config.SECRET_KEY
