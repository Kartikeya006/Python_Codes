# Program to Reverse the Entered String From the Given point position k
a = int(input("Enter Size of Array:-"))
b = int(input("Enter Kth Value of Sub Array Reversal:-"))
f = input("Enter Values:-")
c = list(map(int, f.split()))
if len(c) > a:
    print("You Have entered Numbers out of Range!")
else:
    d = c[0:b]
    d.reverse()
    e = c[b:]
    e.reverse()
    for item in d+e:
        print(item, end="\t")
