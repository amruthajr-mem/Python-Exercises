numbers=[10, 20, 30, 40, 50 ,60, 70, 80, 90, 100]
print(numbers)
print("Before eliminating:" , id(numbers))
i=0
length=(len(numbers))
while i < length :
    if numbers[i] > 50 :
        del numbers[i]
        length -=1
    else:
        i +=1
print(numbers)
print("After eliminating:" , id(numbers))