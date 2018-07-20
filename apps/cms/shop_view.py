from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user
from apps.cms import cms_bp
from apps.forms.food_form import MenuCategoryBaseForm
from apps.forms.shop_forms import Add_Shop
from apps.model.base import db
from apps.model.foods_model import MenuCategory
from apps.model.seller_model import ShopInfo
# 检测商铺id合法化
@login_required
def check_shop_id(sid):
    # 判断当前用户是否有sid的店铺
    shop = ShopInfo.query.filter_by(id=sid).first()
    if shop:
        return shop
#增加店铺信息
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


#添加菜品分类
@cms_bp.route('/add_menu_cate/<sid>/', endpoint='add_menu_cate', methods=['GET', 'POST'])
@login_required
def add_menu_cate(sid):
    form = MenuCategoryBaseForm(request.form)
    if request.method == "POST" and form.validate():
            food = MenuCategory()
            food.setattr(form.data)
            db.session.add(food)
            db.session.commit()
            return redirect(url_for('user.主页'))
    return render_template('add_cate.html',form=form)

#查看菜品信息
@cms_bp.route('/show_menu_cate/<sid>/', endpoint='show_menu_cate', methods=['GET', 'POST'])
@login_required
def show_menu_cate(sid):
    shop = ShopInfo.query.filter_by(id=sid).first()
    cate = MenuCategory()
    datas = cate.query.filter_by(shop_id = int(sid))
    return render_template('show_cate.html',form = datas,shop=shop)
