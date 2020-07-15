# 调查
favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }
questionnaire = ['abc','def','hij','jen']
for i in questionnaire:
    if i in favorite_languages.keys():
        print('谢谢{}参与我们的调查'.format(i))
    else:
        print('{}可以参与我们的调查吗？'.format(i))