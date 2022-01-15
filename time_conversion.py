a = input()
if int(a[0:2]) > 12:
    exit(0)
elif int(a[3:5]) > 59:
    exit(0)
elif int(a[6:8]) > 59:
    exit(0)
if 'PM' in a:
    b = a.split(":")
    c = int(b[0])
    if a[0:2] == "12":
        print(a[0:8])
    else:
        c = c + 12
        print(f"{c}{a[2:8:]}")
if 'AM' in a:
    if a[0:2] == "12":
        print(f"00{a[2:8:]}")
    else:
        print(a[0:8])

