members=['工藤','松田','梅﨑']
print(members)
print(members[0])
print(len(members))#len=length
members.append('山田')#要素の追加
print(members)
members[3]='山崎'#要素の書き換え
print(members)
members.remove('梅﨑')#要素の削除
print(members)
del members[0]#番号指定での削除
print(members)

nums=[10,20,30]
print(sum(nums))#合計
print(sum(nums)/len(nums))#平均 lengthで割っている
