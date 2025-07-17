num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
result = ""
#ask for operation 
operation = input("Choose the operation (+, -, *, /): ")

match operation:
    case "+":
        result = num1 + num2
    case "-":
        result = num1 - num2
    case "*":
        result = num1 * num2
    case "/":
        if num2 == 0:
            print("Cannot divide by zero")
        else:
            result = num1 / num2
    case _:
        print("invalid operation")

print("The result is", result)
