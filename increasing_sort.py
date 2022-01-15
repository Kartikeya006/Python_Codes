# Sort the array of 1's and 0's in non decreasing Order
a = int(input("Enter Number of Elements of List:-"))
b = []
for i in range(a):
    c = int(input("Enter 0 or 1:-"))
    b.append(c)
b.sort()
b.reverse()
print(b)
