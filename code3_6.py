scores={'network':50,'database':70,'security':80}

key=input('追加する科目名を入力しろ＞＞')
if key in scores:
    print('すでに登録済み')
else:
    data=int(input('得点を入植＞＞'))
    scores[key]=data
print(scores)
