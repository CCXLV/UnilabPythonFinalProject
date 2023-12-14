import uuid

from src.extensions import db
from src.models import  User, Role

from flask.cli import with_appcontext
import click

ROLES = ['user', 'admin']

USERS = [
    {
        'username': 'test', 'email': 'test@domain.com', 'password': 'testuser', 'role_id': 1
    },
    {
        'username': 'admin', 'email': 'admin@domain.com', 'password': 'adminuser', 'role_id': 2
    }
]

@click.command('init_db')
@with_appcontext
def init_db():
    click.echo('Database creation in progress')
    db.drop_all()
    db.create_all()
    click.echo('Database was created')

    
@click.command('populate_db')
@with_appcontext
def populate_db():
    click.echo('Roles creation in progress')

    for role in ROLES:
        _role = Role(name=role)
        _role.create()
    
    click.echo('Roles was created')

    click.echo('Users creation in progress')

    for user in USERS:
        _user = User(
            user_id=str(uuid.uuid4())[:8], 
            username=user['username'], 
            email=user['email'], 
            password=user['password'], 
            role_id=user['role_id']
        )
        _user.create()

    click.echo('Users was added in database')