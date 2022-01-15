def kill(k, d):
    d = d-1
    t = d
    while len(k) > 1:
        k.pop(t)
        t = (t+d) % len(k)
    print(f"Last Man Survived in Assault is at {k[0]}th Position.")


a = int(input("Enter Number of Persons:-"))
b = int(input("Enter kth Person that to be killed:-"))
c = list(map(int, range(1, a+1)))
kill(c, b)
