import datetime
def log_habit(habit):
    date = datetime.date.today()
    with open("habit_log.txt", "a") as file:
        file.write(f"{date} - {habit}\n")
def view_log():
    try:
        with open("habit_log.txt", "r") as file:
            return file.read()
    except FileNotFoundError:
        return "No logs found yet."



def remove_last_entry():
    try:
        with open("habit_log.txt", "r") as file:
            lines = file.readlines()
        if not lines:
            return "No entries to remove."
        with open("habit_log.txt", "w") as file:
            file.writelines(lines[:-1])
        return "Last entry removed!"
    except FileNotFoundError:
        return "No log file found."



def count_entries():
    try:
        with open("habit_log.txt", "r") as file:
            return len(file.readlines())
    except FileNotFoundError:
        return 0
