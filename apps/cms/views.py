from _curses import flash


from apps.cms.form import LoginForm,RegisterForm
from apps.model.base import db
from apps.model.users import Users
from . import cms_bp #导入实例化的蓝图对象
from flask import render_template, redirect, url_for


#注册
@cms_bp.route('/reg/',endpoint='注册',methods=['GET','POST'])
def reg():
    form = RegisterForm()
    if form.validate_on_submit():
        user = Users(username=form.username.data,
                        password=form.password.data,
                        email=form.email.data)  # 新添加一个用户到数据库中
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('user.主页'))
    else:
        return render_template('reg.html', title=u'注册', form=form)

#登录
@cms_bp.route('/login/',endpoint='登录',methods=['GET','POST'])
def log():
    form = LoginForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):  # 密码验证成功
            return redirect(url_for('user.主页'))
        flash(u'帐号或者密码错误')
    return render_template('log.html', title='登陆', form=form)
