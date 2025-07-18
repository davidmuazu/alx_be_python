task = input("Enter your task:")
priority = input("Priority (high/medium/low):")
time_bound = input("Is it time-bound (yes or no):")


match priority:
    case "high":
        reminder = f"Remainder: '{task}' is a high priority task."
    case "medium":
       reminder = f"Remainder: '{task}' is a high priority task."
    case "low":
        reminder = f"Remainder: '{task}' is a high priority task."
    case _:
        print("invalid priority entered. Try again")

if time_bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    reminder += " Consider completing it when you have free time."
    
print(reminder)