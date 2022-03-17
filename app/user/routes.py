
from flask import Blueprint, render_template, request, redirect, url_for, flash

user = Blueprint('user', __name__, template_folder='user_templates', url_prefix='/user')

from .user_forms import SignInForm, RegForm

@user.route('/', methods=['GET', 'POST'])
def signin():
    sform = SignInForm()
    if request.method == 'POST':
        if sform.validate_on_submit():

            flash(f'You\'re back! Good ricking job {sform.username.data}!')
            return redirect(url_for('home'))
        else:
            flash(f"C'mon Morty, get it together!")
            return redirect(url_for('user.signin'))
    return render_template('user_signin.html', sform=sform)

@user.route('/register', methods=['GET', 'POST'])
def register():
    rform = RegForm()
    if request.method == 'POST':
        if rform.validate_on_submit():

            flash(f'Registration successful! Good ricking job {rform.first_name}!')
            return redirect(url_for('home'))
        else:
            flash("didn't work!!!!!")

            return redirect(url_for('user.register'))
    
    return render_template('user_reg.html', rform=rform)