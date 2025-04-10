def main():
    return
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

def power(x, y):
    return x ** y

def mod(x, y):
    return x % y



if __name__ == "__main__":
    main()
