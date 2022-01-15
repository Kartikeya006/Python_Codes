a = input()
a = int(a)
b = list()
p = 0
t = 0
for i in range(a):
    e = input()
    d = list(map(int, e.split()))
    b.append(d)
for i in range(len(b)):
    p = p + b[i][i]
s = len(b[0])-1
while s >= 0:
    for i in range(len(b[0])):
        t = t + b[i][s]
        s = s-1
z = abs(p-t)
print(z)
