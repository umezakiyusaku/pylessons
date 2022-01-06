count=0
studentnum=int(input('学生の数を入力しろ>>'))
scorelist=list()
while count<studentnum:
    count+=1
    score=int(input('{}人目の試験の得点を入力>>'.format(count)))
    scorelist.append(score)
print(scorelist)
total=sum(scorelist)
print('平均点は{}点です'.format(total/studentnum))
