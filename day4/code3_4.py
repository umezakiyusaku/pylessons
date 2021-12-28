name=input('名前＞＞')
print('{}さん、こんにちは'.format(name))
food=input('{}さんの好きな食べ物＞＞'.format(name))
if food=='カレー':#かっこがいらない
    print('素敵です、カレーは最高ですよね！！')
else:
    print('私も{}が好きですよ'.format(food))

