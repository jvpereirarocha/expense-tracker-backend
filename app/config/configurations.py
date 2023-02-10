class Config:
    DEBUG = False
    TESTING = False


class DevelopmentConfig(Config):
    DEBUG = True
    PORT = 5050

class TestingConfig(Config):
    TESTING = True

class ProductionConfig(Config):
    pass


