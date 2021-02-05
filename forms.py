from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, EqualTo, Email

class registration(FlaskForm):
    name=StringField("Name", validators=[InputRequired("Name should not be left Empty"), Length(max=30, message="Name should be less than 30 charecters")])
    userID=StringField("UserID", validators=[InputRequired("UserID should not be left Empty"),\
        Length(min=4,max=20, message="Length Should be between 4 to 20 charecters")])
    emailID=StringField("Email ID", validators=[InputRequired("UserID should not be left Empty"), Email("Enter a Valid Email ID")])
    mobileNo=StringField("Mobile Number", validators=[InputRequired("mobile number should not be left Empty"), Length(min=10,max=10,message="Don't include contry code")])
    passwd=PasswordField("Password", validators=[InputRequired("Password Should not be left Empty"), Length(min=8, max=20,message="Password should be between 8-20 charecters")])
    confPasswd=PasswordField("Confirm Password", validators=[EqualTo('passwd',message="Passwords should match")])
    submit=SubmitField("Create Account")

class loginForm(FlaskForm):
    userID=StringField("UserID", validators=[InputRequired("UserID should not be left Empty"),\
        Length(min=4,max=20, message="Length Should be between 4 to 20 charecters")])
    passwd=PasswordField("Password", validators=[InputRequired("Password Should not be left Empty"), Length(min=8, max=20,message="Password should be between 8-20 charecters")])
    submit=SubmitField("Login")