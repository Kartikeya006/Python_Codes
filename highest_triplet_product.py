#  Program to find the highest Product possible using triplets of Elements of Given Array

import itertools
a = int(input("Enter Number of Elements of List:-"))
b = []
for i in range(a):
    c = int(input("Enter an Integer:-"))
    try:
        b.append(c)
    except:
        break
z = []
d = itertools.permutations(b, 3)
for j in list(d):
    k = list(j)
    for n in list(k):
        p = k[0]*k[1]*k[2]
        z.append(p)

z.sort()
print(z)
print("Highest Product possible is ", z[len(z)-1])
