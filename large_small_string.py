a = int(input("Enter Number of Strings:-"))
b = input("Enter Strings(Seperated by Whitespaces):-")
c = list(map(str, b.split()))
d = None
e = None
for item in list(c):
    if d == None:
        d = item
        e = item
    elif len(d) < len(item):
        d = item
    elif len(e) > len(item):
        e = item
print(f"Largest string is {d}")
print(f"Smallest String is {e}")
