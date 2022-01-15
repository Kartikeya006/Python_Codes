a = input()
b = a.split()
d = list()
for word in b:
    h = str()
    letters = list(word)
    for characters in list(letters):
        z = characters
        if z.islower() == True:
            z = z.upper()
        else:
            z = z.lower()
        h = h+z
    d.append(h)
d.reverse()
for item in list(d):
    print(item, end=" ")

