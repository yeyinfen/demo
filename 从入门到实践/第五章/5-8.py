# 以特殊方式跟管理员打招呼
username = ['admin','root','Administrator','user']
for i in username:
    if i == 'admin':
        print('Hello {}, would youlike to see a status report?'.format(i))
    else:
        print('Hello {}, thank you for logging in again'.format(i))
