
from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user, login_required, current_user

from apps.cms import cms_bp
from apps.cms.forms import RegForm, LogForm
from apps.model.base import db
from apps.model.users import Users

#主页
@cms_bp.route('/',endpoint='主页',methods=['GET','POST'])
def index():
    if current_user.is_authenticated:
        print(current_user.username)
    else:
        print('======================')
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
        login_user(user)
        return redirect(url_for('user.主页'))
    return render_template('register.html',form=form)

#登录页面
@cms_bp.route('/log/',endpoint='log',methods=['GET','POST'])
def log():
    form = LogForm(request.form)
    if request.method =="POST" and form.validate():
        user = Users.query.filter(Users.username==form.username.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user)
            nexts = request.args.get('next')
            if not nexts or not nexts.startswith('/'):#判断是否有next,or 判断next开头是否斜线开头(防止重定向攻击)
                nexts = url_for('user.主页')
            return redirect(nexts)
        else:
            form.password.errors = ['用户名或者密码有误']
    return render_template('login.html',form=form)

#注销页面
@cms_bp.route('/logout/', endpoint='logout')
def seller_logout():
    logout_user()
    return redirect(url_for('user.主页'))

#商家资料
@cms_bp.route('/merchants/',endpoint='商家')
@login_required
def merchants():
    return '你点我干嘛'