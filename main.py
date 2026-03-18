from utils import add, sub, multiply, divide, exponent, modulo, floor_divide, absolute

while True:
    op = input("Which calculation would you like to perform? (add, subtract, multiply, divide, exponent, modulo, floor_divide, absolute, exit):\n").lower()

    if op == "exit":
        break

    if op not in ["add", "subtract", "multiply", "divide", "exponent", "modulo", "floor_divide", "absolute"]:
        print("Invalid option!")
        continue

    if op == "absolute":
        num = float(input("Enter the number:\n"))
        result = absolute(num)
    else:
        num1 = float(input("Enter the first number:\n"))
        num2 = float(input("Enter the second number:\n"))

        if op == "add":
            result = add(num1, num2)
        elif op == "subtract":
            result = sub(num1, num2)
        elif op == "multiply":
            result = multiply(num1, num2)
        elif op == "divide":
            result = divide(num1, num2)
        elif op == "exponent":
            result = exponent(num1, num2)
        elif op == "modulo":
            result = modulo(num1, num2)
        elif op == "floor_divide":
            result = floor_divide(num1, num2)

    if isinstance(result, str):
        print(result)
    else:
        print("The result is:", float(result))