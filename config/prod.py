import os
from .default import *


SECRET_KEY = 'df8b3703942a6c6b5ddc8066622ea153a74d8c30a3831fc5e666c7b63cef1eac77421ceeff277ccc'

APP_ENV = APP_ENV_PRODUCTION

#SQLALCHEMY_DATABASE_URI = 'postgres://sulbessarvpslq:35b72cf801d6990aac68d63a85ac4eded659a7e097d4e99c9bfa9cbb56aa3214@ec2-54-246-115-40.eu-west-1.compute.amazonaws.com:5432/d7jt2tm0vhvs0p'

# Heroku - Restriccion:
# The value of your app’s DATABASE_URL config var might change at any time. You should not rely on this value either inside or outside your Heroku app.
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')