# 城市
cities = {'北京':{'country':'中国','population':'2154万人','fact':'中国首都'},
          '纽约':{'country':'美国','population':'854万人','fact':'美国第一大城市'},
          '莫斯科':{'country':'俄罗斯','population':'1420万人','fact':'俄罗斯首府'}}
for k,v in cities.items():
    print('{}的信息：'.format(k))
    print('所属国家：{}'.format(v['country']))
    print('人口数量：{}'.format(v['population']))
    print('城市性质：{}'.format(v['fact']))
