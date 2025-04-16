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
