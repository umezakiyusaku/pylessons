import pprint #これがあることによって表が整えられる

data=[[1,2,3],[4,5,6]]
print(data[1][2]) #[1]の[2]なので答えは6

data=list()
for i in range(10):
    temp=list()
    for j in range(10):
        temp.append(0)
    data.append(temp)
pprint.pprint(data)

w=10
h=10
data=[None]*h
for i in range(h):
    data[i]=[0]*w
pprint.pprint(data)

data=[[0]*w]*h
pprint.pprint(data)

data[1][1]=5
pprint.pprint(data)

data=[[0]*w for i in range(h)]
pprint.pprint(data)

q1=[[100-(i*10+j) for j in range(10)]for i in range(10)]

#2重ループ
for i in range(h):
    temp=[None]*w
    for j in range(w):
        temp[j]=i*10+j+1
    data[i]=temp
pprint.pprint(data)

#内装表記
data=[[i*10 + j for j in range(1,11)] for
i in range(0,10)]
print(data)

#1~7の要素を持つリストを作る
x=[n for n in range(1,8)]
print(x)#[1,2,3,4,5,6,7]

#1~7の要素の2乗した値を持つリストを作る
x=[n**2 for n in range(1,8)]
print(x)#[1,4,9,16,25,36,49]

#1~7の要素の内偶数のリストを作る
x=[n for n in range(1,8) if n %2 ==0]
print(x)#[2,4,6]

#入れ子のforでリストを作る
x=[i*10+j for i in range(1,3) for j in range(2,5)]
print(x)#[12,13,14,22,23,24]

#２次元リストを作る
x=[[i*10+j for j in range(7,10)]for i in range(1,3)]
print(x)#[[17,18,19],[27,28,29]]]

#単位行列生成
row=col=3
matrix=[[1 if i==j else 0 for j in range(col)]for i in range(row)]
print(matrix)#i[[1,0,0],[0,1,0],[0,0,1]]
