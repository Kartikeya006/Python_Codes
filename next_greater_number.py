#  Find the Next greater number with same set of digits as entered Number
import math
import itertools
a = int(input("Enter an Integer:-"))


def seperate(x):  # this function takes an integer as input and returns a list of its digits in same order
    y = int(math.log(x, 10))
    e = []
    for j in range(y + 1):
        f = x % 10
        x = int(x / 10)
        e.append(f)
    e.reverse()
    return e


def joint(y):  # This function takes a list of integers and concatenate its integers to make a single integer
    g = 0
    y.reverse()
    for n, i in enumerate(y):
        k = y[n]*(10**n)
        g = g+k
    return g


b = seperate(a)
c = itertools.permutations(b)
x = []
for i in list(c):
    x.append(i)
w = []
for i in list(x):
    j = list(i)
    u = joint(j)
    w.append(u)
q = set(w)
print(q)
for i in range(a+1, max(q)+1):
    print(i)
    break
