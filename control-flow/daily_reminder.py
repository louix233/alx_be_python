task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        reminder = "'" + task + "' is a high priority task"
    case "medium":
        reminder = "'" + task + "' is a medium priority task"
    case "low":
        reminder = "'" + task + "' is a low priority task"
    case _:
        reminder = "'" + task + "' has an undefined priority"

if time_bound == "yes" and priority in ["high", "medium", "low"]:
    reminder = reminder + " that requires immediate attention today!"
else:
    reminder = reminder + ". Consider completing it when you have free time."

print("\nReminder:", reminder)
