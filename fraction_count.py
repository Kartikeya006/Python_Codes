a = input()
a = int(a)
b = input()
l1 = list()
l2 = list()
l3 = list()
b = list(map(int, b.split()))
for i in list(b):
    if i == 0:
        l1.append(i)
    elif i > 0:
        l2.append(i)
    else:
        l3.append(i)
d = len(b)
print(len(l2)/d)
print(len(l3)/d)
print(len(l1)/d)
