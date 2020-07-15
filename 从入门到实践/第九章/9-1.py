# 餐馆
# 创建餐馆类
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
    @staticmethod
    def open_restaurant():
        print('餐厅正在营业！')


restaurant = Restaurant('读书铺', '酸笋鸡')
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()
