from flask import Blueprint, render_template
from flask_login import login_required

from src.models.post import Post

home_blueprint = Blueprint('main', __name__)


@home_blueprint.route('/')
@login_required
def home():
    posts = Post.query.all()
    
    return render_template('main/home.html', posts=posts)