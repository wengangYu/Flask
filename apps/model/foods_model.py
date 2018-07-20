from apps.model.base import Base, db
#菜品分类
class MenuCategory(Base):
    # 分类名称
    name = db.Column(db.String(32))
    # 分类描述
    description = db.Column(db.String(128), default='')
    # 是否默认
    is_default = db.Column(db.Boolean, default=False)
    # 归属店铺
    shop_id = db.Column(db.Integer, db.ForeignKey('shop_info.id'))
    #设置反向查找关系
    shop = db.relationship('ShopInfo', backref='categories')
    #categories  分类

    def __repr__(self):
        return "<MenuCate {}>".format(self.name)

