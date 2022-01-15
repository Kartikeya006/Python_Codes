a = int(input("Enter First Number:-"))
b = int(input("Enter Second Number:-"))


def eu_gcd(a, b):
    if a == 0:
        return b
    return eu_gcd(b % a, a)


d = eu_gcd(a, b)
print(d)
