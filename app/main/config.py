import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    IMG_BB_KEY = os.getenv('IMG_BB_KEY', '')
    SERP_API_KEY = os.getenv('SERP_API_KEY', '')
    DEBUG = False
    # Swagger
    RESTX_MASK_SWAGGER = False


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    PRESERVE_CONTEXT_ON_EXCEPTION = False


class ProductionConfig(Config):
    DEBUG = False


config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)

