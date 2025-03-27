import math


def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x-1)

l = lambda x, n : pow(-1, n) * pow(x, 2 * n + 1) / factorial(2 * n + 1)

def sine_x(x, n):
    ret = 0
    for i in range(n, -1, -1):
        ret += l(x, i)
    return ret

x = int(input("Enter a number for x in degrees: "))
x = x * (math.pi / 180)
n1 = int(input("Enter a number for n: "))
print("Result of sine for entered values:")
print(sine_x(x, n1))

h_sum = 0

def h_recursive(n):
    """
    Description:
    Recursively calculates Hn = 1 + 1/2 + 1/3 + ... + 1/n
    using a global variable to accumulate the result.

    Parameters:
    n (int): The positive integer up to which Hn should be calculated.

    Returns:
    None: This function modifies the global variable 'h_sum' and returns nothing.
    """
    global h_sum
    if n == 0:
        return
    h_recursive(n - 1)
    h_sum += 1 / n


n1 = int(input("Enter a number for n in Hn: "))
print("Result of Hn for entered value:")
h_recursive(n1)
print(h_sum)





