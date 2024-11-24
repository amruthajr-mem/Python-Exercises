str1= "Python is Awesome"
words= str1.split()
reverse=' '.join(word[::-1] for word in words)
print(reverse)