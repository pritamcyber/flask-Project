from flask_wtf import FlaskForm
from flask_wtf.file import FileField,FileAllowed
from wtforms import StringField,ValidationError, PasswordField,FileField, SubmitField,BooleanField,EmailField,IntegerField
# from wtforms.fields.html5 import EmailField
from flaskblog import db
from flaskblog.models import user,Education

from wtforms.validators import DataRequired, Length, Email, EqualTo
# from email_validator import e
from wtforms import validators 

class RegistrationForm(FlaskForm):
    username = StringField('Username',validators=[Length(min=3,max=20),DataRequired()]) 
    last_name = StringField('Last Name',validators=[Length(min=3,max=20),DataRequired()]) 
    images = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    email = EmailField('Email Address', [validators.DataRequired(), validators.Email()])
    job = StringField('Job Role',validators=[Length(min=3,max=20),DataRequired()]) 

    password = PasswordField('Password',validators=[DataRequired(),Length(min=6,max=10)])
    phone_no = StringField('Phone Number',validators=[Length(min=10,max=10),DataRequired()]) 
    
    confirm_password = PasswordField('Confirm Password',validators=[DataRequired(),EqualTo("password")])
    submit = SubmitField('Sign Up')
    
      
    def validate_username(self, phone_no):
        use= user.query.filter_by(username=phone_no.data).first()
        if use:
            raise ValidationError('That username is taken. Please choose a different one.') 
        # did't understand this validationError thing 

    def validate_email(self, email):
        use = user.query.filter_by(email=email.data).first()
        if use:
            raise ValidationError('That email is taken. Please choose a different one.')
    
    
class LoginForm(FlaskForm):
    
    email = StringField('Email', validators=[DataRequired(),Email()])

    password = PasswordField('Password',validators=[DataRequired(),Length(min=6,max=10)])
    remember = BooleanField('Remenber Me')
    submit = SubmitField('Login')

class educatino_form(FlaskForm):
    Educations = StringField('Education',validators=[DataRequired()]) 

    year_from = StringField('Year From', [validators.DataRequired(),Length(min=4,max=4)])

    year_to = StringField('Year to',validators=[DataRequired(),Length(min=4,max=4)])
    From = StringField('From',validators=[Length(min=10,max=100),DataRequired()]) 
    
    discription = StringField('Discription',validators=[DataRequired()])
    submit = SubmitField('Submit')
    

# class educatoin_form(FlaskForm):
#     From_which=   StringField('Location',validators=[DataRequired()] )
#     education  = StringField('Education' ,validators=[DataRequired()])
#     From = StringField('From_Yaer',validators=[DataRequired()])
#     to = StringField('To_year',validators=[DataRequired()])
#     discription = StringField('discription',validators=[DataRequired()])



    
    