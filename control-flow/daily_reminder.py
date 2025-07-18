task = input("Enter your task: ")
priority = input("priority (high/medium/low): ")
time_bound = input("is it time-bound (yes or no): ")

match priority:
    case "high":
        if time_bound == "yes":
            print(f"Remainder: {task} is a high priority task that requires immediate attention today!")
        else:
            print(f"Note: {task} is a high priority task. Consider completing it when you have free time.")
    case "medium":
        if time_bound == "yes":
            print(f"Remainder: {task} is a medium priority task that should be done today if possible!")
        else:
            print(f"Note: {task} is a medium task. Consider completing it when you have free time.")
    case "low":
        if time_bound == "yes":
            print(f"Note: {task} is a low priority task and is time bound requires attention today!")
        else:
            print(f"Note: {task} is a low priority task. Consider completing it when you have free time.")
    case _:
        print("invalid priority entered. Try again")
print("\n" + "Have a productive day!")