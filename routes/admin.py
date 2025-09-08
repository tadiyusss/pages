from .. import bp
from flask import render_template, request, jsonify, redirect, url_for, flash
from core.utils.decorators import role_required
from flask_login import current_user
from flask_login import login_required
from ..models.contents import Blog, Category, Block
from core.extensions import db
from ..forms.category import CategoryForm
import json

@bp.route('/dashboard/category/delete/<string:uuid>', methods=['GET'])
@role_required(['Administrator', 'Editor'])
@login_required
def delete_category(uuid):
    category = Category.query.filter_by(uuid=uuid).first_or_404()
    db.session.delete(category)
    db.session.commit()
    flash('Category deleted successfully!', 'global-success')
    return redirect(url_for('pages.category'))

@bp.route('/dashboard/category', methods=['GET', 'POST'])
@role_required(['Administrator', 'Editor'])
@login_required
def category():
    form = CategoryForm()
    categories = Category.query.all()
    if request.method == 'POST':
        if form.validate_on_submit():
            category = Category(
                name=form.name.data,
                description=form.description.data,
                created_by=f"{current_user.firstname} {current_user.lastname}"
            )
            db.session.add(category)
            db.session.commit()
            return redirect(url_for('pages.category'))

    return render_template('dashboard/contents/category.html', form=form, categories = categories)

@bp.route('/dashboard/contents', methods=['GET'])
@role_required(['Administrator', 'Editor'])
@login_required
def contents():
    blogs = Blog.query.all()
    return render_template('dashboard/contents.html', blogs=blogs)

@bp.route('/dashboard/contents/delete/<string:uuid>', methods=['GET'])
@role_required(['Administrator', 'Editor'])
@login_required
def delete_content(uuid):
    blog = Blog.query.filter_by(uuid=uuid).first_or_404()
    db.session.delete(blog)
    blocks = Block.query.filter_by(blog_id=blog.id).all()
    for block in blocks:
        db.session.delete(block)
    db.session.commit()
    flash('Content deleted successfully!', 'global-success')
    return redirect(url_for('pages.contents'))

@bp.route('/dashboard/contents/create', methods=['GET'])
@role_required(['Administrator', 'Editor'])
@login_required
def create_content():
    categories = Category.query.all()
    return render_template('dashboard/contents/create.html', categories=categories)


@bp.route('/dashboard/contents/save', methods=['POST'])
@role_required(['Administrator', 'Editor'])
@login_required
def save_content():
    data = request.get_json()
    blog = Blog(
        title = data.get('blog_title'),
        description = data.get('description'),
        thumbnail = data.get('thumbnail'),
        version = data.get('version'),
        category_id = data.get('category') if data.get('category') != 'none' else None,
        author_name = f"{current_user.firstname} {current_user.lastname}"
    )
    db.session.add(blog)
    db.session.commit()
    for block in data.get('blocks', []):
        new_block = Block(
            blog_id=blog.id,
            block_type=block.get('type'),
            data=block.get('data').get('text'),
            
        )
        db.session.add(new_block)
    db.session.commit()

    return jsonify({'message': 'Content saved successfully!'}), 200

