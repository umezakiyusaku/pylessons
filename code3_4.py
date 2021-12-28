name=input('名前＞＞')
print('{}さん、こんにちは'.format(name))
food=input('{}さんの好きな食べ物を教えろ＞＞'.format(name))
if'カレー'in food:
    print('素敵です、カレーは最高よ')
else:
    print('私も{}が好きです'.format(food))

n=10
if n in[5,50,15]:
    print('OK')
else:
    print('ng')

key='red'
if key in{'red':'赤','blue':'青'}:
    print('OK')
    print('ng')
