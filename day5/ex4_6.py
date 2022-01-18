numbers = [1,1]
data = sum(numbers)
count=2
while data <= 1000:
    numbers.append(data)
    data = data+numbers[count-1]
    count+=1
    print(numbers)
