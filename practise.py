r = int(input("Enter Number of Rows Of Matrix :-"))
c = int(input("Enter Number of Columns of Matrix :-"))
a = []
for i in range(r):
    b = []
    for j in range(c):
        b.append(int(input(f"Enter a[{i+1}{j+1}] element of Matrix :-")))
    a.append(b)
for i in range(r):
    for j in range(c):
        print(a[i][j], end=" ")
    print()
