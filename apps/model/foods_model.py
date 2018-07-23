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

# 菜品信息
class MenuFood(Base):
    # 菜品名称
    food_name = db.Column(db.String(64))
    # 菜品评分
    rating = db.Column(db.Float, default=5.0)
    # 归属店铺
    shop_id = db.Column(db.Integer, db.ForeignKey('shop_info.id'))
    # 归属分类
    category_id = db.Column(db.Integer, db.ForeignKey('menu_category.id'))
    cates = db.relationship('MenuCategory', backref='foods')    # 添加一条关系
    shop = db.relationship('ShopInfo', backref='shop')    # 添加一条关系
    # 菜品价格
    food_price = db.Column(db.DECIMAL(6, 2), default=0.0)
    # 菜品描述
    description = db.Column(db.String(128), default='')
    # 月销售额
    month_sales = db.Column(db.Integer, default=0)
    # 评分数量
    rating_count = db.Column(db.Integer, default=0)
    # 提示信息
    tips = db.Column(db.String(128), default='')
    # 菜品图片
    food_img = db.Column(db.String(128), default='')

    def __repr__(self):
        return "<Food: {}-{}>".format(self.food_name, self.food_price)


