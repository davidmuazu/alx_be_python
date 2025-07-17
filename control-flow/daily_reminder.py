task = str(input("Enter task description: "))
priority = str(input("Enter task priority (high/medium/low): "))
time_bound = str(input("is it time-bound (yes or no): "))
remainder = ""

match priority:
    case "high":
        if time_bound == "yes":
            remainder = print(f"Remainder: {task} is a high priority task that requires immediate attention today!")
        else:
            remainder = print(f"Note: {task} is a low priority task. Consider completing it when you have free time.")
    case "medium":
        if time_bound == "yes":
            remainder = print(f"Remainder: {task} is a high priority task that requires immediate attention today!")
        else:
            remainder = print(f"Note: {task} is a low priority task. Consider completing it when you have free time.")
    case "low":
        if time_bound == "yes":
            remainder = print(f"Remainder: {task} is a high priority task that requires immediate attention today!")
        else:
            remainder = print(f"Note: {task} is a low priority task. Consider completing it when you have free time.")