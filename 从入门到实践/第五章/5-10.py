# 检查用户名
current_users = ['root1','root2','root3','root4','root5','root6']
new_users = ['user1','user2','user3','root7','root2','root3']
for i in new_users:
    if i in current_users:
        print('用户名{}已被使用,请重新输入用户名'.format(i))
    else:
        print('用户名{}未被使用'.format(i))
