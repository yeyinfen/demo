# 放眼世界
tourism_city = ['成都','北京','迪拜','杭州','苏州']
print(tourism_city,'第一次打印')
print(sorted(tourism_city),'第一次改变')
print(tourism_city,'第一次核实')
print(sorted(tourism_city,reverse=True),'第二次改变')
print(tourism_city,'第二次核实')
tourism_city.reverse()
print(tourism_city,'第三次改变')
tourism_city.reverse()
print(tourism_city,'第三次核实')
tourism_city.sort()
print(tourism_city,'第五次改变')
tourism_city.sort(reverse=True)
print(tourism_city,'第六次改变')

