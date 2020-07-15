# 电影票
print('不同年龄的观众票价不同，输入quit时结束票价查询')
while True:
    shuru = input('请输入年龄：')
    if shuru == 'quit':
        break
    else:
        if int(shuru) <= 3:
            print('免费')
        elif 3 < int(shuru) < 12:
            print('票价10美元')
        else:
            print('票价15美元')