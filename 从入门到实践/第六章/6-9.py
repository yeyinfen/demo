# 喜欢的地方
favorite_places = {'张三':['昆明','成都'],'赵四':['北京'],'王五':['西安','武汉','杭州']}
for k,v in favorite_places.items():
    print('{}喜欢的城市:'.format(k))
    for i in v:
        print(i)