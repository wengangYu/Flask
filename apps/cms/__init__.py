from flask import Blueprint #引入蓝图

cms_bp =Blueprint('user',__name__,url_prefix='/user') #实例化蓝图


from apps.cms.auth_view import reg,index,log
from apps.cms.shop_view import add_shop,add_menu_cate
