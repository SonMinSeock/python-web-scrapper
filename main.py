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

operation = ""
first_num = ""
second_num = ""

while operation != "exit":
    while True:
        first_num = input("Choose a number: \n")
        if checkInputNum(first_num):
            first_num = int(first_num)
            break
    
    while True:
        second_num = input("Choose another one: \n")
        if checkInputNum(second_num):
            second_num = int(second_num)
            break

    while True:
        operation = input("Choose an operation: \n   Options are: +, -, * or /.\n   Write 'exit' to finish.\n")
        if checkInputOperation(operation):
            break

    if operation != "exit":
        result = calc(first_num, second_num, operation)
        print(f"Result: {result}")