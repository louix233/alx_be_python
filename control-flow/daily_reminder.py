task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        reminder_text = "'" + task + "' is a high priority task"
    case "medium":
        reminder_text = "'" + task + "' is a medium priority task"
    case "low":
        reminder_text = "'" + task + "' is a low priority task"
    case _:
        reminder_text = "'" + task + "' has an undefined priority"

if time_bound == "yes" and priority in ["high", "medium", "low"]:
    reminder_text = reminder_text + " that requires immediate attention today!"
else:
    reminder_text = reminder_text + ". Consider completing it when you have free time."

print("Reminder: " + reminder_text)

