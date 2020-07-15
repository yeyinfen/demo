# 尝试登陆次数
# 创建一个User类
class User:
    def __init__(self, full_name, age, sex):
        self.full_name = full_name
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


u1 = User('张三', 28, '男')
print(u1.login_attempts)
u1.increment_login_attempts()
print(u1.login_attempts)
u1.increment_login_attempts()
print(u1.login_attempts)
u1.increment_login_attempts()
print(u1.login_attempts)
u1.increment_login_attempts()
print(u1.login_attempts)
u1.reset_login_attempts()
print(u1.login_attempts)
