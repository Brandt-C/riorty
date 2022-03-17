
from flask import Blueprint, render_template, request, redirect, url_for, flash

user = Blueprint('user', __name__, template_folder='user_templates', url_prefix='/user')

from .user_forms import SignInForm, RegForm
from app.models import User, db
from werkzeug.security import check_password_hash
from flask_login import login_user, current_user, login_required, logout_user

@user.route('/', methods=['GET', 'POST'])
def signin():
    sform = SignInForm()
    if request.method == 'POST':
        if sform.validate_on_submit():

            user = User.query.filter_by(username=sform.username.data).first()
            if user and check_password_hash(user.password, sform.password.data):
                
                login_user(user)
                flash(f'You\'re back! Bout time {sform.username.data}!', category='success')
                return redirect(url_for('home'))
        
        flash(f"C'mon Morty, get it together! wrong pass or username.")
        return redirect(url_for('user.signin'))
    return render_template('user_signin.html', sform=sform)

@user.route('/register', methods=['GET', 'POST'])
def register():
    rform = RegForm()
    if request.method == 'POST':
        if rform.validate_on_submit():
            newuser = User(rform.username.data, rform.email.data, rform.password.data, rform.first_name.data, rform.last_name.data)
            try:
                db.session.add(newuser)
                db.session.commit()
            except:
                flash(f'Something here has already been used- try something different broh!')
                return redirect(url_for('user.register'))
            login_user(newuser)
            flash(f'Registration successful! Good ricking job {rform.first_name}!', category='success')
            return redirect(url_for('home'))
        else:
            flash("didn't work!!!!!", category='danger')

            return redirect(url_for('user.register'))
    
    return render_template('user_reg.html', rform=rform)