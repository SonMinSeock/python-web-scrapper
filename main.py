# BLUEPRINT | DONT EDIT
playing = True

a = int(input("Choose a number:\n"))
b = int(input("Choose another one:\n"))
operation = input(
    "Choose an operation:\n    Options are: + , - , * or /.\n    Write 'exit' to finish.\n"
)
# /BLUEPRINT

# 👇🏻 YOUR CODE 👇🏻:
def calc(num1, num2, operation):
    result = 0
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        result = num1 / num2
    return result

def checkInputNum(num):
    if not num.isdigit():
        print("Invalid input! Please enter a valid number.")
        return False
    return True

def checkInputOperation(operation):
    if operation not in ["+", "-", "*", "/", "exit"]:
        print("Invalid operation! Please choose from +, -, *, / or exit.")
        return False
    return True    

while playing:
    while not checkInputNum(str(a)):
        a = input("Choose a number:\n")
    a = int(a)
    
    while not checkInputNum(str(b)):
        b = int(input("Choose another one:\n"))
    b = int(b)
    
    while not checkInputOperation(operation):
        operation = input(
            "Choose an operation: \n   Options are: +, -, * or /.\n   Write 'exit' to finish.\n"
        )

    if operation == "exit":
        playing = False
    else:
        result = calc(a, b, operation)
        print(f"Result: {result}")
        
        a = input("Choose a number:\n")
        b = input("Choose another one:\n")
        
        operation = input(
            "Choose an operation:\n    Options are: + , - , * or /.\n    Write 'exit' to finish.\n"
        )