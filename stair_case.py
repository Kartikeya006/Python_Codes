a = input()
a = int(a)
j = a-1
while j >= 0:
    for i in range(j):
        print(" ", end="")
    for i in range(j-1, a-1):
        print("#", end="")
    print()
    j = j-1
