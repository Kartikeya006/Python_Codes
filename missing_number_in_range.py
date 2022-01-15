a = input()
a = list(map(int, a.split()))
a.sort()
max_limit = int(input("Enter Maximum Limit:-"))
min_limit = int(input("Enter Minimum Limit:-"))
print("Missing Numbers are :-", end=" ")
for i in range(min_limit, max_limit+1):
    if i not in list(a):
        print(i, end=" ")
