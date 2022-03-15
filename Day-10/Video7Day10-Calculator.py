# Calculator

# Add
def add(n1, n2):
    return n1 + n2

# Subtract
def subtract(n1, n2):
    return n1 - n2

# Multiply
def multiply(n1, n2):
    return n1 * n2

# Divide
def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    num1 = float(input("What is the first number?: "))
    for symbol in operations:
            print(symbol)
                
    should_countinue = True
    while should_countinue:
        operation_symbol = input("Pick an operation from line above: ")
        num2 = float(input("What is the second number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")
        
        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculations: ") == 'y':
            num1 = answer
        else:
            should_countinue = False
            calculator()

calculator()