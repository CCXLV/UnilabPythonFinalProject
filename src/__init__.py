from flask import Flask

from src.config import Config
from src.models import User, Post
from src.extensions import db, migrate, login_manager
from src.views import home_blueprint, static_blueprint, auth_blueprint, post_blueprint
from src.admin import admin, SecureModelView, UserView, PostView
from src.commands import init_db, populate_db


BLUEPRINTS = [
    home_blueprint,
    static_blueprint,
    auth_blueprint,
    post_blueprint,
]

COMMANDS = [
    init_db, 
    populate_db
]


def create_app():
    app = Flask(__name__, template_folder='templates', static_folder='static')
    app.config.from_object(Config)

    register_extension(app)
    register_blueprints(app)
    register_commands(app)

    return app


def register_extension(app):
    db.init_app(app)

    migrate.init_app(app, db)

    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)  
    
    admin.init_app(app)
    admin.add_view(PostView(Post, db.session))
    admin.add_view(UserView(User, db.session))


def register_blueprints(app):
    for blueprint in BLUEPRINTS:
        app.register_blueprint(blueprint)


def register_commands(app):
    for command in COMMANDS:
        app.cli.add_command(command)