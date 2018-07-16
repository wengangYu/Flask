import os

DEBUG = True

#数据库配置
SQLALCHEMY_DATABASE_URI = 'mysql://root:168668@127.0.0.1:3306/hm_715'
SQLALCHEMY_TRACK_MODIFICATIONS = True
SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'