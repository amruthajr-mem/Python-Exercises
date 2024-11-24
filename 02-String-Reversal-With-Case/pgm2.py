str1= "Python is Awesome"
words = str1.split()
reversed_words=[]
for word in words:
    reversed_char = list(word[::-1])
    for i, char in enumerate(word):
        if char.isupper():
            reversed_char[i]=reversed_char[i].upper()
        else:
            reversed_char[i]=reversed_char[i].lower()
    reversed_words.append("".join(reversed_char))
result = ' '.join(reversed_words)
print(result) 