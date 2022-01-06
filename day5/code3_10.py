print('すべての質問にyまたはnで答えろ')
kanearuka=input('金あんのか？')
if kanearuka=='y':
 onakasuiteruka=input('お腹すいてるか？')
 nomitaikibunnka=input('ビール飲みたい？')
 if onakasuiteruka=='y'and nomitaikibunnka=='y':
     print('焼肉はいかが？')
 elif onakasuiteruka=='y':
    print('カレーはいかが？')
 elif nomitaikibunnka=='y':
    print('焼き鳥はいかが？')
 else:
    print('パスタはいかが？')
 yasyokuiruka=input('夜食はいりますか？')
 if yasyokuiruka=='y':
    print('コンビニ飯はいかが？')
else:
    print('家で食べましょう。')

