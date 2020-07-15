# 熟食店
sandwich_orders = ['ham and cheese sandwich','sausage sticks sandwich','tuna sandwich']
finished_sandwiches = []
a = 'I made your {}'
for i in  sandwich_orders:
    print(a.format(i))
while sandwich_orders:
    finished_sandwiche = sandwich_orders.pop()
    finished_sandwiches.append(finished_sandwiche)
print(finished_sandwiches)


