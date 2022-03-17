from flask import Blueprint, redirect, render_template, request, jsonify, url_for, flash
from flask_login import current_user
from app.models import db, User, Post
from .blogforms import PostForm

blog = Blueprint('blog', __name__, template_folder='blog_templates', url_prefix='/blog')

@blog.route('/<string:username>', methods=['GET', 'POST'])
def userProfile(username):
    user = User.query.filter_by(username=username).first()
    if user:
        posts = Post.query.filter_by(user_id=user_id).order_by(Post.timestamp.desc()).all()
    else:
        return render_template('userprofile.html', User=None, posts=None)
    
    form  = PostForm()
    if request.method == 'POST' and current_user.id.is_authenticated:
        if current_user.id == user.id and form.validate_on_submit():
            newpost = Post()
            newpost.body = form.new_post.data
            newpost.user_id = current_user.id   

            db.session.add(newpost)
            db.session.commit()
            flash('New post made!')
            return redirect(url_for('blog.userProfile', username=current_user.username))

        else:
            return jsonify({'What are you doing here?': 'This is NOT where you belong.'}), 403
    return render_template('userprofile.html', user=user, posts=posts)


    

