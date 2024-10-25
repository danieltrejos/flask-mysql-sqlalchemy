import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'clave_secreta'
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
    DEBUG = os.getenv('DEBUG',False)
    #SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_ECHO = True  # Útil para ver las consultas SQL en modo desarrollo

class ProjectConfig(Config):
    DEBUG = False
    SQLALCHEMY_ECHO = False