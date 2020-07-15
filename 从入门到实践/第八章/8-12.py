# 三明治
def make_sandwich(*ingredients):
    print('请核对你提供的食材:')
    for i in ingredients:
        print('--',i)


make_sandwich('eggplant', 'tomato', 'egg')
make_sandwich('吐司','番茄','火腿','乳酪','牛油')
make_sandwich('鸡蛋','吐司','洋葱','茄子','番茄','面粉','高汤','生菜叶')