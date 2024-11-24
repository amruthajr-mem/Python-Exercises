numbers_list=[10, 20, 60, 30, 20, 40, 30, 60, 70, 80]
import collections
duplicates = []
count_list=collections.Counter(numbers_list)
for i, count in count_list.items():
    if count > 1:
        duplicates.append(i)
print(numbers_list)
print(duplicates)