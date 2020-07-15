# 冰淇淋小店
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


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    # 显示冰淇淋
    def describe_IceCream(self):
        print('冰淇淋口味有：\n', self.flavors)


a = ['奶油冰淇淋', '酸奶冰淇淋', '果蔬冰淇淋', '奇异果冰淇淋']
i = IceCreamStand(flavors=a, restaurant_name='可口',cuisine_type=0)
i.describe_IceCream()
