from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class VerifyForm(FlaskForm):
	articletext = StringField('Article Text')
	submit = SubmitField("Verify")