from environs import Env

env = Env()
env.read_env()


class Config:
    LOG_LEVEL = "debug"
    SECRET_KEY = env.str("SECRET_KEY", "")
    SQLALCHEMY_DATABASE_URI = env.str("DATABASE_URL", "")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
