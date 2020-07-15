# 创建一个User类
class User:
    def __init__(self, age, sex):
        self.full_name = '张三'
        self.age = age
        self.sex = sex
        self.login_attempts = 0

    # 描述简单的个人信息
    def describe_user(self):
        print('姓名：{}'.format(self.full_name))
        print('性别：{}'.format(self.sex))
        print('年龄：{}'.format(self.age))

    # 问候
    def greet_user(self):
        if self.sex == '男':
            print('{}先生，祝你生活愉快！'.format(self.full_name))
        else:
            print('{}女士，祝你生活愉快！'.format(self.full_name))

    # 增加登陆次数
    def increment_login_attempts(self):
        self.login_attempts += 1

    # 重置登陆次数
    def reset_login_attempts(self):
        self.login_attempts = 0


class Admin(User):
    """重写__init__方法的时候调用父类默认值，不使用其他参数的时候"""
    def __init__(self, privileges):
        super().__init__(age=None, sex=None)
        self.privileges = privileges

    def show_privileges(self):
        print('{}你的权限有：'.format(self.full_name))
        for i in self.privileges:
            print(i)


b = ['can add post', 'can delete post', 'can ban user']
a = Admin(privileges=b)
a.show_privileges()
