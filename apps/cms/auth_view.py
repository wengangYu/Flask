from _curses import flash
from flask import render_template, request, redirect, url_for, session
from apps.cms import cms_bp
from apps.cms.forms import RegForm, LogForm
from apps.model.base import db
from apps.model.users import Users

#主页
@cms_bp.route('/',endpoint='主页',methods=['GET','POST'])
def index():
    return render_template('index.html')
#注册
@cms_bp.route('/reg/',endpoint='reg',methods=['GET','POST'])
def reg():
    form = RegForm(request.form)
    if request.method == 'POST' and form.validate():
        user = Users()
        user.setattr(form.data)
        db.session.add(user)
        db.session.commit()
        session['is_login'] = True
        session['u_name'] = user.username
        session['uid'] = user.id
        return redirect(url_for('user.主页'))
    return render_template('register.html',form=form)

#登录页面
@cms_bp.route('/log/',endpoint='log',methods=['GET','POST'])
def log():
    form = LogForm(request.form)
    if request.method =="POST" and form.validate():
        user = Users.query.filter(Users.username==form.username.data).first()
        if user is not None and user.verify_password(form.password.data):
            session['is_login'] = True
            session['u_name'] = user.username
            session['uid'] = user.id
            return redirect(url_for('user.主页'))
        else:
            form.password.errors = ['用户名或者密码有误']
    return render_template('login.html',form=form)

#注销页面
@cms_bp.route('/logout/', endpoint='logout')
def seller_logout():
    session.clear()
    return redirect(url_for('user.主页'))