from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from src.models.base import BaseModel
from src.extensions import db


class User(BaseModel, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    _user_id = db.Column(db.String)
    username = db.Column(db.String)
    email = db.Column(db.String)
    _password = db.Column(db.String)

    role_id = db.Column(db.ForeignKey('roles.id'))
    role = db.relationship('Role', uselist=False)


    @property
    def password(self):
        return self._password
    
    @password.setter
    def password(self, psw):
        self._password = generate_password_hash(psw)

    def check_password(self, psw):
        return check_password_hash(self.password, psw)
    
    def is_admin(self):
        return self.role and self.role.name == 'admin'
    
    @property
    def user_id(self):
        return self._user_id
    
    @user_id.setter
    def user_id(self, u_id):
        self._user_id = u_id
    

class Role(BaseModel):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    def __repr__(self):
        return f'{self.name}'