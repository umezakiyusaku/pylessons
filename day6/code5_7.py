def hello(name):
    print('こんにちは{}です'.format(name))
hello('浅木')
hello('梅﨑')

def profile(name,age,hobby):
    print('私の名前は{}です。'.format(name))
    print('年齢は{}です'.format(age))
    print('趣味は{}です'.format(hobby))
profile('梅﨑','22','将棋')

def plus(x,y):
    answer=x+y
    return answer
answer=plus(100,50)
print('足し算の答えは{}です'.format(answer))
    
