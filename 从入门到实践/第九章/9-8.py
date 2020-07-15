# 权限
# 创建一个Privileges类
class Privileges:
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    # 显示权限
    def show_privileges(self):
        print('拥有的权限：')
        for i in self.privileges:
            print(i)
# 创建Admin类
class Admin:
    def __init__(self):
        self.privileges = Privileges()


a = Admin()
a.privileges.show_privileges()
