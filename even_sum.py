# Write a Program to pick three numbers from the given array such that their Sum is even
import itertools
a = int(input("Enter Range of Numbers"))
b = list()
for i in range(1, a+1):
    b.append(i)
b = list(itertools.combinations(b, 3))
c = list()
count = 0
for i in list(b):
    if sum(i) % 2 == 0:
        count += 1
print(count)
