import os
from os import environ

class Config(object):

    DEBUG=False
    TESTING=False

    basedir=os.path.abspath(os.path.dirname(__file__))

    SECRET_KEY='Sidhant'

    UPLOADS="C:\Users\wahan\Desktop\image_watermarking\app"
    SESSION_COOKIE_SECURE=True

    DEFAULT_THEME=None

class DevelopmentConfig(Config):
    DEBUG=True
    SESSION_COOKIE_SECURE=False

class DebugConfig(Config):
    DEBUG=False
