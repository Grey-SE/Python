import art

print(art.logo)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def calculator(first_input, second_input):
    calculator_functions = {
        "+": add(first_input, second_input),
        "-": subtract(first_input, second_input),
        "*": multiply(first_input, second_input),
        "/": divide(first_input, second_input)
    }

    if math_operator in calculator_functions:
        print(f"{first_input} {math_operator} {second_input} = {calculator_functions[math_operator]}")
        return calculator_functions[math_operator]
    return None


isRunning = True
input1 = float(input("Enter first number: "))

while isRunning:

    input2 = float(input("Enter second number: "))
    math_operator = input("Enter an operator (+, -, *, /): ")

    result = calculator(int(input1), int(input2))

    yes_or_no = input(f"Type 'y' to continue calculating with {result}, "
                      f"type 'n' to start a new calculation, "
                      f"or type 'q' to quit").lower()

    if yes_or_no == "y":
        input1 = result
    elif yes_or_no == "n":
        input1 = float(input("Enter first number: "))
        continue
    else:
        isRunning = False
        print("Goodbye!")
