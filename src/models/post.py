from src.models.base import BaseModel
from src.extensions import db


class Post(BaseModel):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String)
    title = db.Column(db.String)
    content = db.Column(db.String)
    _date = db.Column(db.DateTime)
    

    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, dt):
        self._date = dt
