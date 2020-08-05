import logging
from flask import abort, render_template, current_app
from werkzeug.exceptions import NotFound

from . import public_bp
from app.models import Post

logger = logging.getLogger(__name__)

@public_bp.route("/")
def index():
    logger.info('Mostrando los posts del blog')

    posts = Post.get_all()
    return render_template("public/index.html", posts=posts)


@public_bp.route("/p/<string:slug>/")
def show_post(slug):
    logger.info('Mostrando un post')
    logger.debug(f'Slug: {slug}')
    
    post = Post.get_by_slug(slug)
    if post is None:
        raise NotFound(slug)
    return render_template("public/post_view.html", post=post)