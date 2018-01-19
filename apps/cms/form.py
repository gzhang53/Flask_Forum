from wtforms import Form,StringField,IntegerField
from wtforms.validators import Email,InputRequired,Length,EqualTo

class LoginForm(Form):
    email = StringField(validators=[Email(message="please enter correct email"),InputRequired(message="please enter your email")])
    password =StringField(validators=[Length(6,20,message='please enter a password between 6 and 20 characters')])
    remember = IntegerField()

class ResetpwdForm(Form):
    oldpwd = StringField(validators=[Length(6, 20, message='please enter a your old password')])
    newpwd = StringField(validators=[Length(6, 20, message='please enter a new password ')])
    newpwd = StringField(validators=[Length(6, 20, message='please enter a new password')])