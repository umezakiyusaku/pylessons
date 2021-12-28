members=['梅﨑']#要素数１のリスト
scores={'network':82}#要素数１のディレクショナリ
members=('梅﨑')
print(type(members))
members=('梅﨑',)#要素数の１のタプルの正しい定義。後ろに,をつけている
print(type(members))
person=tuple('山田')
print(type(person))#こちらでも可能。
