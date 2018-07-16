from werkzeug.security import generate_password_hash, check_password_hash

from .base import db, Base


class Users(Base):
    username = db.Column(db.String(32),unique=True,nullable=False)
    password = db.Column(db.String(128),nullable=False)
    # password_hash = db.Column(db.String(128), nullable=True)          # 模型中加入密码散列值
    email = db.Column(db.String(64), nullable=True, unique=True)     # 新建一个邮箱字段


    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter      # 设置password属性的值时，赋值函数会调用generate_password_hash函数
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)
    def __repr__(self):
        return 'Users -{}'.format(self.username)