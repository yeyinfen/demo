# 专辑
def make_album(name,album_name,num=''):
    if num:
        dict1 = {name: [album_name,'专辑数量:'+ num]}
    else:
        dict1 = {name: album_name}
    return dict1


a = make_album('周杰伦','稻香','7')
print(a)
a = make_album('刀郎','那一夜')
print(a)
a = make_album('周深','大鱼')
print(a)