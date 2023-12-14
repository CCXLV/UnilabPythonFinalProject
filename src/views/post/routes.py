from datetime import datetime

from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user

from src.models.post import Post
from src.views.post.forms import CreatePostForm

post_blueprint = Blueprint('posts', __name__)


@post_blueprint.route('/post', methods=['GET', 'POST'])
@login_required
def create_post():
    form = CreatePostForm()
    if form.validate_on_submit():
        post = Post(author=current_user.username, title=form.title.data, content=form.content.data, date=datetime.now())
        post.create()

        return redirect(url_for('main.home'))
    
    return render_template('post/post.html', form=form)


@post_blueprint.route('/posts', methods=['GET', 'POST'])
@login_required
def posts():
    _posts = Post.query.all()

    return render_template('post/posts.html', posts=_posts)
