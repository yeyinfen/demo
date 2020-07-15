# 不变的魔术师
def make_great(name):
    name1 = []
    for i in name:
        a = str(i) + 'the Great'
        name1.append(a)
    print(name1)



names = ['user1', 'user2', 'user3', 'user4', 'user5', 'user6' ]
make_great(names[:])