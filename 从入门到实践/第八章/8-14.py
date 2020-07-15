


# 汽车
def make_car(**kwargs):
    print('汽车基本信息')
    for k,v in kwargs.items():
        print('{}:{}'.format(k,v))


make_car(品牌='比亚迪',型号='宋Pro',内饰='超豪华',动力='新能源')
user_profile(姓名='叶子',年龄=26,性别='男',星座='射手座')