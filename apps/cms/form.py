# -*- coding:utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, Length, EqualTo

#登陆表
class LoginForm(FlaskForm):
    email = StringField(label='邮箱',validators=[DataRequired(), Length(1,64), Email()], id='loginlength')
    name = StringField(label='用户名:',validators=[DataRequired(), Length(1,64),], id='loginlength')
    password = PasswordField(label='密码:',validators=[DataRequired()], id='loginlength')
    submit = SubmitField(label='登陆')

#注册表
class RegisterForm(FlaskForm):
    email = StringField(label='邮箱地址',validators=[DataRequired(), Length(1,64), Email()], id='registerlength')
    username = StringField(label='用户名',validators=[DataRequired(), Length(1,64)],
                           id='registerlength')
    password = PasswordField(label='密码',validators=[DataRequired(),
                                                     EqualTo('password2', message='密码必须相同')], id='registerlength')
    password2 = PasswordField(label='确认密码',validators=[DataRequired()], id='registerlength')
    submit = SubmitField(label='马上注册')