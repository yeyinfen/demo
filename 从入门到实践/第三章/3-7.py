# 缩减名单
roster = ['小猪','吴波','王震','赵四']
message = ',邀请你一起共进晚餐!'
roster.insert(0,'王二')
roster.insert(3,'张三')
roster.append('闰土')

print('对不起大家，餐桌无法送达我只能邀请两位跟我进餐')
message1 = '，很抱歉，下次在邀请你'
roster1 = roster.pop()
print(roster1 + message1)
roster1 = roster.pop()
print(roster1 + message1)
roster1 = roster.pop()
print(roster1 + message1)
roster1 = roster.pop()
print(roster1 + message1)
roster1 = roster.pop()
print(roster1 + message1)
print(roster[0] + message)
print(roster[1] + message)
del roster[0]
print(roster)
del roster[0]
print(roster)

