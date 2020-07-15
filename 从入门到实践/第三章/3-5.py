# 修改嘉宾名单
roster = ['小猪', '吴波', '王震', '赵四']
message = ',邀请你一起共进晚餐!'
print('我们刚刚得知' + roster[1] + '无法到场')
roster[1] = '张三'
print(roster[0] + message)
print(roster[1] + message)
print(roster[2] + message)
print(roster[3] + message)