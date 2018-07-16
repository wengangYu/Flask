from flask import Blueprint #引入蓝图
cms_bp =Blueprint('user',__name__,url_prefix='/user') #实例化蓝图

from .index_view import index
from .views import reg,log