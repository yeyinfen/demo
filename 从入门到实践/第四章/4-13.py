# 自助餐
buffet = ('红烧肉','青椒土豆丝','番茄炒蛋','炒白菜','拍黄瓜')
for i in buffet:
    print('------>',i)
# buffet[1] = '青椒炒肉'  TypeError: 'tuple' object does not support item assignment
buffet = ('红烧肉','青椒土豆丝','番茄炒蛋','青椒炒肉','腌菜洋芋丝')
for x in buffet:
    print(x)
