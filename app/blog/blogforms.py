from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, EqualTo, Email



class PostForm(FlaskForm):
    new_post = StringField('Post', validators=[DataRequired()])
    submit = SubmitField()