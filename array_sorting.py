# Write a Program to sort the given array
a = input("Enter Array:-")
a = list(map(int, a.split()))
b = list()
for i in range(min(a), max(a)+1):
    if i in list(a):
        b.append(i)
print(b)
