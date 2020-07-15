# 用户的专辑
def make_album(name,album_name,num=''):
    if num:
        dict1 = {name: [album_name,'专辑数量:'+ num]}
    else:
        dict1 = {name: album_name}
    return dict1


while True:
    print('输入q可以退出')
    name = input('请输入歌手名字：')
    if name == 'q':
        break
    album_name = input('请输入专辑名字：')
    if album_name == 'q':
        break
    a = make_album(name=name,album_name=album_name)
    print(a)