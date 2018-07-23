from flask_login import current_user
from wtforms import Form, StringField, validators, BooleanField, SelectField, DecimalField

# 菜品分类验证器
from apps.model.seller_model import ShopInfo


class MenuCategoryBaseForm(Form):
    name = StringField(label="菜品分类名",
                       validators=[
                           validators.InputRequired(message="请输入菜品分类名"),
                           validators.Length(max=32, message="不能超过32字符"),
                       ])
    # 分类描述
    description = StringField(label="菜品分类描述",
                              validators=[
                                  validators.Length(max=128, message="不能超过32字符"),
                              ])
    # 是否默认
    is_default = BooleanField(label="是否默认")
    # 关联店铺


# 菜品信息验证器
class MenuFoodBaseForm(Form):
    # 菜品名称
    food_name = StringField(label="菜品名称",
                            validators=[
                                validators.InputRequired(message="请输入菜品分类名"),
                                validators.Length(max=64, message="不能超过32字符"),
                            ])
    # 归属分类
    category_id = SelectField(label="菜品分类", coerce=int)
    # 菜品价格
    food_price = DecimalField(label="菜品价钱", places=2,
                              validators=[validators.NumberRange(min=0, max=9999, message="价钱超出范围"),
                                          validators.InputRequired(message="请输入菜品价格"),
                                          ]
                              )
    # 菜品描述
    description = StringField(label="菜品描述",
                              validators=[
                                  validators.Length(max=128, message="不能超过128字符"),
                              ])
    # 提示信息
    tips = StringField(label="菜品提示信息",
                       validators=[
                           validators.Length(max=128, message="不能超过32字符"),
                       ])

    def __init__(self, sid, *args, **kwargs):
        super(MenuFoodBaseForm, self).__init__(*args, **kwargs)
        if current_user.is_authenticated:
            shop = ShopInfo.query.get(sid)
            self.category_id.choices = [(cate.id, cate.name) for cate in shop.categories]
