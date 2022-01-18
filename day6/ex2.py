
def min_max(n,*args):
    maxN,minN=n,n
    for i in args:
        if i > maxN:
            maxN=i
        if i < minN:
            minN=i
    return maxN,minN

maxN,minN = min_max(3,4,1,5,3)
print(f'最大{maxN},最小{minN}')

hikisuu=input(int('好きな数字をカンマ区切りで5つ入力'))
