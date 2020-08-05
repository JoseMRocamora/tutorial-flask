from os.path import abspath, dirname

# Define the application directory
BASE_DIR = dirname(dirname(abspath(__file__)))

# Aplicacion 
SECRET_KEY = '5eb861997206962e77f24379ea1b2552fc85769bf72843bf813a6578ee6a01c4'

# Database configuration
SQLALCHEMY_TRACK_MODIFICATIONS = False

# App environments
APP_ENV_LOCAL = 'local'
APP_ENV_TESTING = 'testing'
APP_ENV_DEVELOPMENT = 'development'
APP_ENV_STAGING = 'staging'
APP_ENV_PRODUCTION = 'production'
APP_ENV = ''
