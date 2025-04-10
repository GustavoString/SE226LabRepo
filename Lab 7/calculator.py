import math_utils

def main():
    operations = {
        '+': math_utils.add,
        '-': math_utils.subtract,
        '*': math_utils.multiply,
        '/': math_utils.divide,
        '**': math_utils.power,
        '%': math_utils.mod
    }

    x = int(input("Enter a value for x: "))
    y = int(input("Enter a value for y: "))

    operator = input("Enter a operator: ")

    if operator in operations:
        print("The result of ", x, operator, y, "is:", operations[operator](y, x))
    else:
        print("Invalid operator")

if __name__ == "__main__":
    main()