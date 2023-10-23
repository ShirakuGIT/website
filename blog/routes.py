from flask import render_template, Blueprint
from .models import Post

bp = Blueprint('main', __name__)

@bp.route("/post/<int:post_id>")
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', post=post)
