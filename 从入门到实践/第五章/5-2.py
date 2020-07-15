# 更多的条件测试
a = 'a'
print(a == 'a')
print(a != 'a')
print('-' * 20)
b = 'abc'
print(b.lower() == 'Abc')
print(b.lower() != 'Abc')
print('-' * 20)
c = 18
print(c <= 20)
print(c >= 20)
print(c == 18)
print(c != 18)
print('-' * 20)
d = 'ABCD'
print(d.upper() and  d == 'ABCD')
print(d.title() or d == 'ABCD')
print('-' * 20)
f = 'qwer'
print('q' in f )
print('q' not in f)