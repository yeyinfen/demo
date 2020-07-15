# 你的披萨和我的披萨
my_pizza = ['奥尔良烤鸡披萨','水果披萨','海鲜披萨']
friend_pizza = my_pizza[:]
my_pizza.append('至尊披萨')
friend_pizza.append('火腿披萨')
print('My favorite pizzas are:',my_pizza)
print('Myfriend favorite pizzas are:',friend_pizza)
for i in my_pizza:
    print(i)