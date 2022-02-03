import random,time
lotts = ['{:04d}'.format(i) for i in range(10000)]

n = int(input('宝くじを何枚買いますか？＞＞'))
my_lotts = sorted(random.sample(lotts,n),reverse=True)
print(my_lotts)


lucky = '{:04d}'.format(random.randrange(10000))
print('抽選開始...')
print(lucky[0])#先頭のモジ
for c in lucky:
    time.sleep(1)
    print(c)

result = [[] for i in range(4)]#二次元リスト
for lott in my_lotts:
    if lucky == lott:#lucky番号と同じだったら
        result[0].append(lott)#０に挿入する
    elif lucky[-3:]==lott[-3:]:
        result[1].append(lott)
    elif lucky[-2:]==lott[-2:]:
        result[2].append(lott)
    elif lucky[-1]==lott[-1]:
        result[3].append(lott)

for i in range(len(result)):
    print('{}等賞({:*>4s})'.format(i+1,lucky[i:]),result[i])#resultを取り出す、resultが０の時は1等賞

