# 尝试使用各个函数，每个本章函数都使用一遍
tourist_place = ['杭州','苏州','北京','成都','罗筱韩']
print(tourist_place)
# .append()函数列表末尾添加元素
tourist_place.append('汽车')
print(tourist_place)
# .insert()函数列表指定下标添加元素
tourist_place.insert(3,'自由')
print(tourist_place)
# del语句，根据指定下标删除列表元素
del tourist_place[1]
print(tourist_place)
# .pop()弹出列表元素，不指定下标时弹出末位，指定时弹出指定位置元素
a = tourist_place.pop()
print(a)
print(tourist_place)
# .remove()删除指定元素
tourist_place.remove('自由')
print(tourist_place)
# .sort()对列表按照字母排序，是永久的，reverse=True时是反向排序
tourist_place.sort()
print()
tourist_place.sort(reverse=True)
print(tourist_place)
# sorted()对列表临时排序
sorted(tourist_place,reverse=True)
print(tourist_place)
# 反转列表元素
tourist_place.reverse()
print(tourist_place)
# len()获得列表长度
print(len(tourist_place))
# 下标跟reverse()效果一致
tourist_place = tourist_place[::-1]
print(tourist_place)

