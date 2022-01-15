# Program to compare the half diagonal sum of the Entered Odd order square matrix
a = int(input("Enter The Number of Rows of a Square Matrix:-"))
v4 = 0
v5 = 0
v1 = 0
v3 = 0
if a % 2 == 0:
    print("Half Diagonal Sum Comparison is not possible in even order matrix!")
else:
    b = list()
    for i in range(a):
        d = list()
        for j in range(a):
            c = int(input(f"Enter {i+1}{j+1}th Element:-"))
            d.append(c)
        b.append(d)
    for i in range(a):
        for j in range(a):
            print(b[i][j], end=" \t")
        print("\n")
    for i in range(int(a/2)):
        v1 = v1+b[i][i]
    v2 = b[int(a/2)][int(a/2)]
    i = a-1
    while i > int(a/2):
        v3 = v3 + b[i][i]
        i -= 1
    i = a-1
    j = 0
    while i > int(a/2) > j:
        v4 = v4 + b[i][j]
        v5 = v5 + b[j][i]
        i = i-1
        j = j+1
    if v1 == v2 == v3 == v4 == v5:
        print("YES")
    else:
        print("NO")
