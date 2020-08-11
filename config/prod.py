from .default import *


SECRET_KEY = 'df8b3703942a6c6b5ddc8066622ea153a74d8c30a3831fc5e666c7b63cef1eac77421ceeff277ccc'

APP_ENV = APP_ENV_PRODUCTION

SQLALCHEMY_DATABASE_URI = 'postgresql://db_user:db_pass@host:port/db_name'