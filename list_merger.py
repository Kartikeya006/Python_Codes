#  Merge K sorted lists and return a one sorted list
a = int(input("Enter Number of Lists:-"))
d = []
for i in range(a):
    x = int(input("Enter Number of List Elements:-"))
    b = []
    for j in range(x):
        c = int(input("Enter List Elements:-"))
        b.append(c)
    b.sort()
    d = d+b
d.sort()
print(d)
