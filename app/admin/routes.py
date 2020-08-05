from flask import render_template, redirect, url_for
from flask_login import  current_user, login_required

from . import admin_bp
from .forms import PostForm
from app.models import Post


@admin_bp.route("/admin/post/", methods=['GET', 'POST'], defaults={'post_id': None})
@admin_bp.route("/admin/post/<int:post_id>/", methods=['GET', 'POST'])
@login_required
def post_form(post_id):
    form = PostForm()
    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data

        post = Post(user_id=current_user.id, title=title, content=content)
        post.save()

        return redirect(url_for('public.index'))
    return render_template("admin/post_form.html", form=form)
    