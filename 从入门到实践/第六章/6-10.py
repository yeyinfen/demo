# 喜欢的数字
lucky_number = {'刘一':[1,23,4],'陈二':[5,2,53],'张三':[43,1,65],'李四':[5,63],'王五':[24,75],'赵六':[24,53,6]}
for k,v in lucky_number.items():
    print('{}喜欢的幸运数字是：'.format(k))
    for i in v:
        print(i)