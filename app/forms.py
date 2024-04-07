# Add any form classes for Flask-WTF here
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField 
from wtforms.validators import InputRequired 
from flask_wtf.file import FileField, FileAllowed , FileRequired




class MovieForm(FlaskForm):
    title = StringField('Username', validators=[InputRequired()])
    description = PasswordField('Password', validators=[InputRequired()])
    poster = FileField('Image Upload', validators=[
        FileRequired(message='Please select a file to upload.'),
        FileAllowed(['jpg', 'png' , 'jpeg'], message='Only JPG and PNG images are allowed.')
    ])
