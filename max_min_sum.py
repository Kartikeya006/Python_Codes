import itertools
a = input()
a = list(map(int, a.split()))
b = itertools.permutations(a, 4)
d = list()
for i in list(b):
    d.append(sum(i))
print(min(d), max(d))
