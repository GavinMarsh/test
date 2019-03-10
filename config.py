## MongoEngine Note: include db name in URI; it overwrites all others

class Config(object):
    MONGODB_HOST = 'mongodb://localhost:27017/gm-sandbox'
    DEBUG = False
    TESTING = False

class ProductionConfig(Config):
    MONGODB_HOST = 'mongodb://localhost:27017/gm-sandbox'

class DevelopmentConfig(Config):
    MONGODB_HOST = 'mongodb://localhost:27017/gm-sandbox'
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
