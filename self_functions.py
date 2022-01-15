import math
import itertools


def seperate(x):  # this function takes an integer as input and returns a list of its digits in same order
    y = int(math.log(x, 10))
    e = []
    for j in range(y + 1):
        f = x % 10
        x = int(x / 10)
        e.append(f)
    e.reverse()
    return e


def replace(z):  # This function takes a list and replace a number in list by another number and returns modified list
    a = int(input("Enter Number to replace:-"))
    b = int(input("Enter replacement Number:-"))
    for n, i in enumerate(z):
        if i == a:
            z[n] = b
    return z


def joint(y):  # This function takes a list of integers and concatenate its integers to make a single integer
    g = 0
    y.reverse()
    for n, i in enumerate(y):
        k = y[n]*(10**n)
        g = g+k
    return g


def first_last(c):  # This function takes an integer as Input and returns its first and last digit
    b = int(math.log(c, 10))
    print("Last Digit is ", c % 10)
    print("First digit is ", c // (10 ** b))


def possible_numbers(z):  # This function takes a list of integer and returns a list containing all possible Numbers
    b = []
    y = itertools.permutations(z)
    for i in list(y):
        b.append(i)
    return b


def convert(y):  # This function convert a tuple in a list(Can be used only for tuple in a list)
    for i in y:
        for i in range(len(y)):
            y[i] = list(y[i])
    return y


def print_matrix(z):    # This function print the values of list in the list in form of Matrix
    for i in range(len(z)):
        for j in range(len(z)):
            print(z[i][j], end=" ")
        print()


def transpose(c):       # This function change the original Matrix to its Transpose
    for i in range(len(c)):
        for j in range(i, len(c)):
            c[i][j], c[j][i] = c[j][i], c[i][j]


def spiral_matrix(m, n, f):     # Print the Matrix in spiral form
    k = 0                       # m is number of rows
    l = 0                       # n is number of columns
    while k < m and l < n:
        for i in range(l, n):
            print(f[k][i], end=" ")
        k += 1
        for i in range(k, m):
            print(f[i][n-1], end=" ")
        n -=1
        if k < m:
            for i in range(n-1, (l-1), -1):
                print(f[m-1][i], end=" ")
        m -= 1
        if l < n:
            for i in range(m-1, k-1, -1):
                print(f[i][l], end=" ")
            l += 1
