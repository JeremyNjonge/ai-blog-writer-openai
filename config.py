##OPEN API STUFF
OPENAI_API_KEY = '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'



## FLASK STUFF
class Config(object):
    DEBUG = True
    TESTING = False

class DevelopmentConfig(Config):
    SECRET_KEY = "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"


config = {
    'development': DevelopmentConfig,
    'testing': DevelopmentConfig,
    'production': DevelopmentConfig
}
