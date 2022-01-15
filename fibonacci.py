a = int(input("Enter Number of Fibonacci Terms:-"))
b = list()
for j in range(0, a):
    if j == 0:
        b.append(0)
    elif j == 1:
        b.append(1)
    else:
        i = b[j-1]+b[j-2]
        b.append(i)
print(b)
