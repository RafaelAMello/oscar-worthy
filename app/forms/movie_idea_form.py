from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class NewMovieIdea(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = StringField('description', validators=[DataRequired()])