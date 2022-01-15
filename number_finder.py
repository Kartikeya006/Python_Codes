#  Given an Unsorted array of size N find First Element such that it is smaller than right one and Greater Than left one

a = int(input("Enter Size of Array:-"))
b = []
for i in range(a):
    c = int(input("Enter Element Of Array:-"))
    try:
        b.append(c)
    except:
        break
for j in range(1, len(b)):
    if b[j-1] < b[j] < b[j+1]:
        print(b[j])
        break
    else:
        continue
