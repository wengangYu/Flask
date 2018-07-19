from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user
from apps.cms import cms_bp

#商家资料
from apps.forms.shop_forms import Add_Shop
from apps.model.base import db
from apps.model.shop_info import ShopInfo


@cms_bp.route('/add_shop/',endpoint='开店',methods = ["GET","POST"])
@login_required
def add_shop():
    print(1121)
    form = Add_Shop(request.form)
    if request.method == "POST" and form.validate():
        shop = ShopInfo()
        shop.setattr(form.data)
        shop.seller_id = current_user.id
        db.session.add(shop)
        db.session.commit()
        return redirect(url_for('user.主页'))
    return render_template('add_shop.html',forms=form)