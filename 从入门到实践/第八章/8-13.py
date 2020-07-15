# 用户简介
def user_profile(**kwargs):
    print('个人基本信息')
    for k,v in kwargs.items():
        print('{}:{}'.format(k,v))


# user_profile(姓名='叶子',年龄=26,性别='男',星座='射手座')
