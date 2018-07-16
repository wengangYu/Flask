from flask import Flask
from apps.cms import cms_bp
from apps.model.base import db
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from apps.model.users import Users

# login_manager = LoginManager()
# login_manager.session_protection = 'strong'
# login_manager.login_view = 'user.主页'
def create_app():
    app = Flask(__name__)
    # login_manager.init_app(app)
    #配置app
    app.config.from_object('myconf')
    #bootstrap初始化
    Bootstrap(app)
    #数据库插件注册到app上
    db.init_app(app)
    #注册蓝图
    app.register_blueprint(cms_bp)

    return app
# @login_manager.user_loader
# def load_user(user_id):
#     return Users.query.get(int(user_id))