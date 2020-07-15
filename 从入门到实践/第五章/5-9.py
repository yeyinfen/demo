# 处理没有用户的情形
username = ['admin','root','Administrator','user']
for i in username:
    if i == 'admin':
        print('Hello {}, would youlike to see a status report?'.format(i))
    else:
        print('Hello {}, thank you for logging in again'.format(i))
del username[:]
if len(username) < 1:
    print('We need to find some users!')

