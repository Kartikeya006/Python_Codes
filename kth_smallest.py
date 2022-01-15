#  Given a list and a number k, where k is smaller than size of list, find kth smallest number of list
a = int(input("Enter Size of List:-"))
b = []
for i in range(a):
    c = int(input("Enter An Integer:-"))
    b.append(c)
b.sort()
k = int(input(f"Enter the Number less than {a} to find kth smallest Number:-"))
print(f"{k}th smallest Number is", b[k-1])
