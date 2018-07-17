from flask_login import LoginManager
from apps.model.users import Users
#实例化这个函数
login_manager = LoginManager()
login_manager.login_view = 'user.log'
#设置回调函数
@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(user_id)