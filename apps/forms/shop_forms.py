from wtforms import StringField, FloatField, validators, Form, DecimalField, BooleanField

#增加店铺
class Add_Shop(Form):
    shop_name = StringField(label='店铺名字',
                            validators=[validators.InputRequired(message='请输入店铺名称'),validators.Length(3,12,message='请输入3-12个字符的店铺名称')],
                            render_kw={'class': 'form-control', 'placeholder': '请输入店铺名称'})
    start_cost = DecimalField(label='起送价格',validators=[validators.InputRequired(message='请输入起送价格')],render_kw={'class': 'form-control', 'placeholder': '请输入起送价格'})
    shipping_fee = DecimalField(label='配送费',validators=[validators.InputRequired(message='请输入配送价格')],render_kw={'class': 'form-control', 'placeholder': '请输入配送价格'})
    shop_notice = StringField(label='店铺公告',
                              validators=[validators.InputRequired(message='请输入您店铺公告'),validators.Length(max=128,message='请不要超过128位以内的字符')],
                              render_kw={'class': 'form-control', 'placeholder': '请输入店铺公告'})
    discounts = StringField(label='优惠信息',validators=[validators.InputRequired(message='请输入优惠活动信息'),validators.Length(4,128,message='优惠信息控制在128位以内')],
                            render_kw={'class': 'form-control', 'placeholder': '请输入优惠信息'})
    is_ontime = BooleanField(label="准时送达", default=False)
    is_bird = BooleanField(label="蜂鸟快递", default=False)
    is_bao = BooleanField(label="提供保险", default=False)
    is_fp = BooleanField(label="提供发票", default=False)
    is_zun = BooleanField(label="准标识", default=False)