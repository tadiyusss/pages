from .. import bp
from flask import render_template
from ..models.contents import Blog, Block, Category

@bp.route('/', methods=['GET'])
def index():
    blogs = Blog.query.all()
    return render_template('index.html', blogs=blogs)


@bp.route('/blog/<string:uuid>', methods=['GET'])
def view_blog(uuid):
    blog = Blog.query.filter_by(uuid=uuid).first_or_404()
    blocks = Block.query.filter_by(blog_id=blog.id).all()

    return render_template('view_blog.html', blog=blog, blocks=blocks)