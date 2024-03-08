from flask_wtf import FlaskForm
from wtforms import FileField, StringField, PasswordField
from wtforms.validators import InputRequired
from flask_wtf.file import FileAllowed, FileRequired, FileField


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])

class UploadForm(FlaskForm):
    photo = FileField('Photo', validators=[
    FileRequired(),
    FileAllowed(['jpg', 'png'], 'Images only!')])