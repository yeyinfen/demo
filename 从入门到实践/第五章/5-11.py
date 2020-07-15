# 序数
list1 = [i for i in range(1,10)]
for x in list1:
    if x == 1:
        print('{}st'.format(x))
    elif x == 2:
        print('{}nd'.format(x))
    elif x == 3:
        print('{}rd'.format(x))
    else:
        print('{}th'.format(x))