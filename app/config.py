import os

# Alembic
ALEMBIC = {
    'script_location': '../migrations'
}

#JWT
JWT_ACCESS_TOKEN_EXPIRES = 1200 # 20 minutes
JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'super-secret')
JWT_VERIFY_SUB = False

#SQLALCHEMY
SQLALCHEMY_ENGINES = {
    'default': os.getenv('DATABASE_URI', 'postgresql://username:password@localhost/dbname')
}
SQLALCHEMY_TRACK_MODIFICATIONS = False