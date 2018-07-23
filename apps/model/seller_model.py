from apps.model.base import Base, db

#商铺信息
class ShopInfo(Base):
    #店铺名字
    shop_name = db.Column(db.String(32),unique=True)
    #起送价格
    start_cost = db.Column(db.Float,default=0.0)
    #配送费
    shipping_fee = db.Column(db.Float,default=0.0)
    #店铺公告
    shop_notice = db.Column(db.String(128),default='欢迎,欢迎,热烈欢迎')
    #优惠信息
    discounts = db.Column(db.String(128),default='')
    # 是否是品牌
    is_brand = db.Column(db.Boolean, default=False)
    # 是否准时送达
    is_ontime = db.Column(db.Boolean, default=True)
    # 是否蜂鸟配送
    is_bird = db.Column(db.Boolean, default=True)
    # 是否保险
    is_bao = db.Column(db.Boolean, default=False)
    # 是否有发票
    is_fp = db.Column(db.Boolean, default=True)
    # 是否准标识
    is_zun = db.Column(db.Boolean, default=False)
    # 店铺logo
    shop_logo = db.Column(db.String(128), default='')
    # 店铺评分
    shop_rating = db.Column(db.Float, default=5.0)
    #关联商家
    seller_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    # 建立一个反向关系
    seller = db.relationship("Users", backref="shop")

    def keys(self):
        return "shop_name", "start_cost", "shipping_fee", "shop_notice", "discounts", "is_ontime", \
               "is_bird", "is_bao", "is_fp", "is_zun"



    def __repr__(self):
        return "<ShopInfo-{}>".format(self.shop_name)

