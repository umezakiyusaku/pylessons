temp=list()
for n in range(10):
    data=float(input('{}個目のデータを入力>>'.format(n+1)))
    temp.append(data)
print(temp[1])

for count in range(len(temp)):
    print('{}時 {}度'.format(count+8,temp[count]))

tempnew=list()
for count in range(len(temp)):
    if count==5:
        tempnew.append('N/A')
    else:
        tempnew.append(temp[count])
print(temp)
print(tempnew)

total=0
for data in tempnew:
    if isinstance(data,float):
        total=total+data
        print(total/(len(tempnew)-1))

