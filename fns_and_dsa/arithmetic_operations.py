result = ""
def perform_operation(num1, num2, operation):
    global result
    if operation == "add":
        result = num1 + num2
    elif operation == "subtract":
        result = num1 - num2
    elif operation == "multiply":
        result = num1 * num2
    elif operation == "divide":
        if num2 == 0:
            return "Error: cannot divide by zero"
        else:
            result == num1 / num2
    else:
        result == "unrecognised value"

    return result
#perform_operation(num1=2, num2=4, operation="subtract")
#print(result)