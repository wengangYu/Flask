
from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user, login_required, current_user

from apps.cms import cms_bp
from apps.forms.user_forms import RegForm, LogForm
from apps.model.base import db
from apps.model.users import Users

#主页
@cms_bp.route('/',endpoint='主页',methods=['GET','POST'])
def index():
    shop=[]
    if current_user.is_authenticated:
        shop = current_user.shop
    return render_template('index.html',stores=shop)
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
    u = request.args.get('user')
    form = LogForm(request.form)
    if request.method =="POST" and form.validate():
        user = Users.query.filter(Users.username==form.username.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user)
            nexts = request.args.get('next')
            if not nexts or not nexts.startswith('/'):#判断是否有next,or 判断next开头是否斜线开头(防止重定向攻击)
                nexts = url_for('user.主页')+'?user={}'.format(current_user.id)
            return redirect(nexts)
        else:
            form.password.errors = ['用户名或者密码有误']
    return render_template('login.html',form=form)

#注销页面
@cms_bp.route('/logout/', endpoint='logout')
def seller_logout():
    logout_user()
    return redirect(url_for('user.主页'))

