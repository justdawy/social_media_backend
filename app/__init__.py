import os

from pathlib import Path
from flask import Flask

BASE_DIR = Path(__file__).resolve().parent.parent
DOCS_DIR = os.path.join(BASE_DIR, 'docs/')

from .extensions import db, alembic, jwt, ma, swagger
from .models import User, Post
from .cli import register_cli


def create_app(config_file='config.py'):
    app = Flask(__name__)
    app.config.from_pyfile(config_file)
    
    db.init_app(app)
    alembic.init_app(app)
    jwt.init_app(app)
    ma.init_app(app)
    swagger.init_app(app)
    
    register_cli(app)
    
    from .routes.auth import auth_bp
    from .routes.users import users_bp
    from .routes.posts import posts_bp
    
    app.register_blueprint(auth_bp)
    app.register_blueprint(users_bp)
    app.register_blueprint(posts_bp)
    
    return app