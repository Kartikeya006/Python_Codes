# you are given an integer and you have to convert all zeros to number 5
import math
a = int(input("Enter an Integer:-"))
b = int(math.log(a, 10))
for i in range(1, b+1):
    c = a % (10**i)
    if i == 1:
        if c == 0:
            a = a+5
    else:
        if c//10**(i-1) == 0:
            a = a+5*(10**(i-1))
    continue
print(a)
