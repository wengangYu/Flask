from flask import render_template, request, redirect, url_for

from apps.cms import cms_bp
from apps.cms.forms import RegForm
from apps.model.base import db
from apps.model.users import Users


@cms_bp.route('/',endpoint='主页',methods=['GET','POST'])
def index():
    return render_template('index.html')

@cms_bp.route('/reg/',endpoint='reg',methods=['GET','POST'])
def reg():
    form = RegForm(request.form)
    if request.method == 'POST' and form.validate():
        user = Users()
        print(user)
        print(12345)
        user.setattr(form.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('user.主页'))

    return render_template('register.html',form=form)