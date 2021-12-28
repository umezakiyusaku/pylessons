scores={'network':60,'database':70,'security':80}
del scores['security']#ディレクトリの削除
print(scores)
total=sum(scores.values())#現段階での合計を表示
print(total)
