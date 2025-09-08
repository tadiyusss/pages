from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from core.styles import Style
from wtforms.validators import DataRequired, Length


class CategoryForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(max=100)], render_kw={"class": Style.text_input})
    description = TextAreaField('Description', validators=[Length(max=500)], render_kw={"class": Style.textarea})
    submit = SubmitField('Create Category', render_kw={"class": Style.button})