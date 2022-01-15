# To print the first and last digit of an Integer
import math
a = int(input("Enter an Integer:-"))
b = int(math.log(a, 10))
print("Last Digit is ", a % 10)
print("First digit is ", a//(10**b))
