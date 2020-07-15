# 使用多个循环
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice cream')
for i in my_foods:
    print('我最爱吃的食物是：',i)
for x in friend_foods:
    print('我朋友最爱吃的食物是：',x)