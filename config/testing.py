from .default import *


# Parámetros para activar el modo debug
TESTING = True
DEBUG = True

APP_ENV = APP_ENV_TESTING

WTF_CSRF_ENABLED = False

# Definir en instance/consig-testing.py la cadena de conexion 
# a la BBDD de test.
#SQLALCHEMY_DATABASE_URI = 'postgresql://db_user:db_pass@host:port/db_name'