from flask_login import current_user
from wtforms import Form, StringField, validators, BooleanField,SelectField


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
    shop_id = SelectField(label='所属店铺',coerce=int)
    def __init__(self,*args,**kwargs):
        super(MenuCategoryBaseForm,self).__init__(*args,**kwargs)
        self.shop_id.choices = []
        if current_user.is_authenticated:
            self.shop_id.choices = [(shop.id, shop.shop_name) for shop in current_user.shop]
