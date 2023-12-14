from os import path

class Config:
    BASE_DIRECTORY = path.abspath(path.dirname(__file__))
    SECRET_KEY = '7d6eaf201c8b13a9f65e91d40615b902'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + path.join(BASE_DIRECTORY, 'database.db')