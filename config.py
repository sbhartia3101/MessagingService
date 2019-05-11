import os
from dotenv import load_dotenv

class Config(object):
    basedir = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    DEBUG = False

    load_dotenv()
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    # SQLALCHEMY_DATABASE_URI = "postgresql://postgres:@localhost/emotive_ai"
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    TWILIO_ACCOUNT = os.getenv('TWILIO_ACCOUNT')
    TWILIO_TOKEN =os.getenv('TWILIO_TOKEN')
    TWILIO_SSID = os.getenv('TWILIO_SSID')
    TWILIO_NUMBER = os.getenv('TWILIO_NUMBER')

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False