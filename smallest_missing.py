# Program to Find Smallest Missing Number in a Given Array
a = int(input("Enter The array Element:-"))
b = []
while True:
    try:
        b.append(a)
        a = int(input("Enter Array Element:-"))
    except:
        break
b.sort()
c = max(b)
for i in range(1, c+2):
    if i in list(b):
        continue
    else:
        print("Missing Number is ", i)
        break
