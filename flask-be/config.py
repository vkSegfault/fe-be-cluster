from decouple import config


class Config:
    SQLACHEMY_TRACK_MODIFICATIONS = config('SQLACHEMY_TRACK_MODIFICATIONS', cast=bool)

class DevConfig(Config):
    DEBUG = True
    SQLACHEMY_ECHO = True   # print SQL commands when executed
    SQLALCHEMY_DATABASE_URI = f"postgresql://{config('DB_USERNAME')}:{config('DB_PASSWORD')}@localhost:5432/{config('DB_NAME')}"

class ProdConfig(Config):
    pass

class TestConfig(Config):
    pass