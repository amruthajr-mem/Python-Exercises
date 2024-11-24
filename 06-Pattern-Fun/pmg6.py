row= int(input('Enter the number of rows:'))
i=1
for value in range(row, -1, -1):
    result =' '.join([str(i) for _ in range(value)])
    print(result)
    i +=1