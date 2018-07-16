from flask import Flask
from apps.cms import cms_bp
from apps.model.base import db
from flask_bootstrap import Bootstrap
def create_app():
    app = Flask(__name__)
    #配置app
    app.config.from_object('myconf')
    #bootstrap初始化
    Bootstrap(app)
    #数据库插件注册到app上
    db.init_app(app)
    #注册蓝图
    app.register_blueprint(cms_bp)
    return app