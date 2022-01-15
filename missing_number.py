# Find The Smallest Positive Number Missing From the List
a = int(input("Enter Number of Elements In List:-"))
b = []
for i in range(a):
    c = int(input("Enter An Integer:-"))
    b.append(c)
d = min(b)
e = max(b)
for j in range(d, e+1):
    if j in list(b):
        continue
    else:
        print("Smallest Missing Number is ", j)
        break
