result = ""
def perform_operation(num1, num2, operation):
    global result
    match operation:
        case "add":
            result = num1 + num2
        case "subtract":
            result = num1 - num2
        case "multiply":
            result = num1 * num2
        case "divide":
            if num2 == 0:
                return "Error: Cannot divide by zero"
            else:
                return num1 / num2
        case _:
            result = "unrecognised value"
    return result
#perform_operation(num1=2, num2=4, operation="subtract")
#print(result)