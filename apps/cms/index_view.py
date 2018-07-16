from . import cms_bp #导入实例化的蓝图对象
from  flask import render_template
@cms_bp.route('/',endpoint='主页',methods=['GET','POST'])
def index():
    return render_template('index.html')