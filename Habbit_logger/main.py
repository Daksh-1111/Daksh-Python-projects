from habit import log_habit, view_log

print("1. Log new habit\n2. View log")
choice = input("Choose an option: ")

if choice == "1":
    habit = input("Enter your habit: ")
    log_habit(habit)
    print("Habit logged!")
elif choice == "2":
    print("Habit log:")
    print(view_log())
else:
    print("Invalid choice.")
