from flask import render_template, request, redirect, url_for,abort
from flask_login import login_required, current_user
from werkzeug.datastructures import MultiDict

from apps.cms import cms_bp
from apps.forms.food_form import MenuCategoryBaseForm, MenuFoodBaseForm
from apps.forms.shop_forms import  AddShopForm
from apps.model.base import db
from apps.model.foods_model import MenuCategory, MenuFood
from apps.model.seller_model import ShopInfo
# 检测商铺id合法化
@login_required
def check_shop_id(sid):
    # 判断当前用户是否有sid的店铺
    shop = ShopInfo.query.filter_by(id=sid,seller_id=current_user.id).first()
    if shop:
        return shop          #这种方法,就会导致我随意串改用户ID号,别人都能看到其他店铺的信息.
    # if not shop:
    #     raise abort(404)    #这种方法会导致有用户及时没有店铺,但是也会报404.体验感很差
    # return shop

#增加店铺信息
@cms_bp.route('/add_shop/',endpoint='开店',methods = ["GET","POST"])
@login_required
def add_shop():
    form = AddShopForm(request.form)
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
    shop = check_shop_id(sid)
    form = MenuCategoryBaseForm(request.form)
    if request.method == "POST" and form.validate():
            food = MenuCategory()
            food.setattr(form.data)
            food.shop_id=shop.id
            db.session.add(food)
            db.session.commit()
            return redirect(url_for('user.主页'))
    return render_template('add_cate.html',form=form,shop=shop)

#查看菜品分类
@cms_bp.route('/show_menu_cate/<sid>/', endpoint='show_menu_cate', methods=['GET', 'POST'])
@login_required
def show_menu_cate(sid):
    shop = ShopInfo.query.filter_by(id=sid).first()
    result = db.session.query(
        MenuCategory.name, db.func.count(MenuFood.id),(db.func.avg(MenuFood.food_price))).join(MenuFood).filter(
        MenuCategory.shop_id == sid).group_by(MenuCategory.name).all()
    print(result)
    return render_template('show_cate.html',form=result,shop=shop)

#添加菜品信息
@cms_bp.route('/add_food/', endpoint='add_food', methods=['GET', 'POST'])
@login_required
def add_food():
    shop_id = request.args.get('shop_id',0)
    shop = check_shop_id(shop_id)
    if shop:
        form = MenuFoodBaseForm(shop_id,request.form)
    else:
        return redirect(url_for('user.主页'))
    if request.method == 'POST' and form.validate():
        food = MenuFood()
        food.setattr(form.data)
        food.shop_id = shop_id
        db.session.add(food)
        db.session.commit()
        return redirect(url_for('user.add_food')+'?shop_id={}'.format(shop_id))
    return render_template('add_food.html',form=form,shop=shop)

#查看菜品信息
@cms_bp.route('/show_food/<sid>', endpoint='show_food', methods=['GET', 'POST'])
@login_required
def show_food(sid):
    shop = check_shop_id(sid)
    #获取该店铺下的所有分类
    cates = MenuCategory.query.filter_by(shop_id=sid).all()
    foods = [(food.name,food.foods)for food in cates]
    return render_template('show_food.html',items=foods,shop=shop)


#主页查看菜品信息
@cms_bp.route('/index_food/', endpoint='index_food', methods=['GET', 'POST'])
@login_required
def index_food():
    u = request.args.get('user')
    print(u)
    check_shop_id(u)
    #查询用户下的店铺名称-菜品分类-菜品表
    shop = ShopInfo.query.filter_by(seller_id=u).all() #用户下的所有店铺表
    return render_template('index_food.html',shops=shop)

#更新菜品分类
@cms_bp.route('/update_shop/<int:sid>', endpoint='update_shop', methods=['GET', 'POST'])
@login_required
def update_shop(sid):
    shop = check_shop_id(sid)
    # form = AddShopForm(data=dict(shop))
    # for x in form:
    #     print(x)
    if request.method =='GET':
        form = AddShopForm(data=dict(shop))
        print(dict(shop))
    else:
        form=AddShopForm(request.form)
        if request.method=='POST' and form.validate():
            s = ShopInfo()
            s.setattr(form.data)
            db.session.add(s)
            db.session.commit()
            return redirect(url_for('user.主页'))
    return render_template('update_shop.html',forms=form)
