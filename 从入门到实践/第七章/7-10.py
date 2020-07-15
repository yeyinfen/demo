# 梦想的度假胜地
a = 'If you could visit one place in the world, where would you go?:'
survey_results = {}
print('hello,We are doing a survey about resorts, help us fill it out')
while True:
    print('输入quit的时候退出')
    # if name == 'quit' or vacation_spot == 'quit':
    #     break
    name = input('请输入调查人名字：')
    if name == 'quit':
        break
    vacation_spot = input(a)
    if  vacation_spot == 'quit':
        break
    survey_results[name] = vacation_spot
    print(survey_results)

