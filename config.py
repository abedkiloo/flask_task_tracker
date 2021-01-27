class Config(object):
    """
       Common configurations
       """


class DevConfig(Config):
    """
       Development configurations
       """

    DEBUG = True
    SQLALCHEMY_ECHO = True


class ProdConfig(Config):
    """
    Production configurations
    """

    DEBUG = False


app_config = {
    'development': DevConfig,
    'production': ProdConfig
}
