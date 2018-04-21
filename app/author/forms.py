'''
@author：KongWeiKun
@file: forms.py
@time: 18-4-20 下午3:31
@contact: kongwiki@163.com
'''
from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    PasswordField,
    BooleanField,
    ValidationError,
    SubmitField
)
from wtforms.validators import DataRequired, Required,Regexp,Length, EqualTo, URL

from app.models import  User


#登录表单
class LoginForm(FlaskForm):
    username = StringField("Username", [DataRequired(), Length(max=255)])
    password = PasswordField("Password", [DataRequired()])
    remember_me = BooleanField('remember_me')
    submit = SubmitField('Log in')

    def validate(self):
        """Validator for check the account information."""
        check_validata = super(LoginForm, self).validate()

        # If validator no pass
        if not check_validata:
            return False

        # Check the user whether exist.
        user = User.query.filter_by(username=self.username.data).first()
        if not user:
            self.username.errors.append('Invalid username or password.')
            return False

        # Check the password whether right.
        if not user.check_password(self.password.data):
            self.username.errors.append('Invalid username or password.')
            return False

        return True


#注册表单
class RegistrationForm(FlaskForm):
    username = StringField("Username",
                           validators=[DataRequired(),Length(1,64),
                        Regexp('^[A-Za-z][A-Za-z0-9_.]*$',0,
                               'Usernames must have only letters, ')])
    password = PasswordField("Password", validators=[DataRequired(),EqualTo('password2'
                                                                            ,message='Password mubst match.')])
    password2=PasswordField('Confirm password',validators=[DataRequired()])
    submit=SubmitField('Register')

    def validate_username(self,filed):
        if User.query.filter_by(username=filed.data).first():
            raise ValidationError('Username Already register')