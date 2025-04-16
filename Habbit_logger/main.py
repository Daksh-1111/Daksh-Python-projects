from habit import log_habit, view_log, remove_last_entry, count_entries
print("Habit Logger")
print("1. Log new habit")
print("2. View log")
print("3. Remove last entry")
print("4. Log habit for specific date")
print("5. Count total habits")
choice = input("Choose an option: ")
if choice == "1":
    habit = input("Enter your habit: ")
    log_habit(habit)
    print("✅ Habit logged!")
elif choice == "2":
    print("📄 Your Habits:")
    print(view_log())
elif choice == "3":
    print(remove_last_entry())
elif choice == "4":
    date = input("Enter date (YYYY-MM-DD): ")
    habit = input("Enter your habit: ")
    log_habit(habit, date)
    print(f"✅ Habit logged for {date}!")


elif choice == "5":
    print(f"Total habits logged: {count_entries()}")
else:
    print(" Invalid choice.")
