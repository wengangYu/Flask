from wtforms import Form, StringField, PasswordField, validators
from wtforms.validators import Email, EqualTo


class RegForm(Form):
    email =StringField(validators=[validators.InputRequired(message='请输入有效字段'),validators.Length(3,16,message='请输入3-16位的邮箱账号'),
                                   Email(message='请输入正确的邮箱地址')])

    username = StringField(validators=[validators.InputRequired(message='请输入有效字段'),validators.Length(3,16,message='请输入3-16位的用户名')])

    password = PasswordField(validators=[validators.InputRequired(message='请输入有效字段'),validators.Length(6,12,message='请输入6-12位密码')])

    password1 = PasswordField(validators=[validators.InputRequired(message='请输入有效字段'),validators.Length(6,12,message='请输入6-12位密码'),
                                          EqualTo('password',message='两次密码不一致')])