from flask_script import Manager
from apps import create_app
from apps.model.base import db
from flask_migrate import Migrate,MigrateCommand
#实例化创建app的函数
app = create_app()
#导入Manager并实例化
manager = Manager(app)
#实例化迁移migrate
migrate = Migrate(app,db)
#增加迁移命令道manager上
manager.add_command('db',MigrateCommand)

if __name__ == '__main__':
    print(app.url_map)
    manager.run()
