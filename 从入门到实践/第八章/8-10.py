# 了不起的魔术师
names = ['user1', 'user2', 'user3', 'user4', 'user5', 'user6', ]


def show_magicians(name):
    for i in name:
        print(i)


def make_great(name1):
    name = []
    for i in name1:
        a = str(i) + 'the Great'
        name.append(a)
    print(name)


make_great(names)

