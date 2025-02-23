# task_reminder.py

# Dictionary to store tasks
tasks = {}

# Function to add a task
def add_task(name, deadline):
    tasks[name] = deadline
    print(f"Task '{name}' added with deadline {deadline}")

# Function to show all tasks
def show_tasks():
    print("\nTask List:")
    for task, deadline in tasks.items():
        print(f"{task}: Due {deadline}")

# Adding sample tasks
add_task("Submit report", "2025-03-01")
add_task("Team meeting", "2025-02-28")

# Display tasks
show_tasks()
