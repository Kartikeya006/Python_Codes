# Sum of Elements between k1th and k2th smallest values
a = input()
a = list(map(int, a.split()))
a.sort()
print(a)
k1th = int(input("Enter First kth Number:-"))
k2th = int(input("Enter Second kth Number:-"))
a = a[k1th:k2th-1]
print(a)
print(f"Sum of Numbers between {k1th}th and {k2th}th number is {sum(a)}")
