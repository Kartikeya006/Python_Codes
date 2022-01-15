a = int(input("Enter Number of Inputs :-"))
b = input("Enter Inputs :-")
b = list(map(int, b.split()))
output = b[0]
b.remove(b[0])
for i in list(b):
    output = output & i
print(output)
