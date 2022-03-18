
from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField
from wtforms.validators import DataRequired

class epCreate(FlaskForm):
    ep_desc = StringField("It's your episode broh, what's going on?", validators=[DataRequired()] )
    # s_choice = 
    # b_choice =
    # j_choice = 
    
class FindChar(FlaskForm):
    id = IntegerField('Choose an id to see a character', validators=[DataRequired()])
    submit = SubmitField()