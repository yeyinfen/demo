# 用户
# 创建一个User类
class User:
    def __init__(self, full_name, age, sex):
        self.full_name = full_name
        self.age = age
        self.sex = sex

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


u1 = User('张三', 29, '男')
u1.describe_user()
u1.greet_user()
u2 = User('赵四', 25, '女')
u2.describe_user()
u2.greet_user()
u3 = User('王五', 36, '男')
u3.describe_user()
u3.greet_user()