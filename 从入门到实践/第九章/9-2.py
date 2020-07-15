# 三家餐馆
#  创建餐馆类
class Restaurant:
    # 初始化属性
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    # 描述餐馆
    def describe_restaurant(self):
        print('这家餐馆叫{}'.format(self.restaurant_name))
        print('招牌菜是：{}'.format(self.cuisine_type))

    # 餐馆正在营业
    def open_restaurant(self):
        print('餐厅正在营业！')


restaurant1 = Restaurant('读书铺', '酸笋鸡')
restaurant2 = Restaurant('滇铺子','杀猪菜')
restaurant3 = Restaurant('菌彩','菌菇火锅')
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()