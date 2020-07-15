# 就餐人数
# 创建餐馆类
class Restaurant:
    # 初始化属性
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    # 描述餐馆
    def describe_restaurant(self):
        print('这家餐馆叫{}'.format(self.restaurant_name))
        print('招牌菜是：{}'.format(self.cuisine_type))

    # 餐馆正在营业
    def open_restaurant(self):
        print('餐厅正在营业！')
        print('现在就餐人数{}'.format(self.number_served))

    # 修改就餐人数
    def set_number_served(self, number_served):
        self.number_served = number_served

    # 就餐人数递增
    def increment_number_served(self, served):
        self.number_served += served


restaurant = Restaurant('读书铺', '酸笋鸡')
restaurant.open_restaurant()
restaurant.set_number_served(20)
restaurant.open_restaurant()
restaurant.increment_number_served(20)
restaurant.open_restaurant()
restaurant.increment_number_served(10)
restaurant.open_restaurant()
