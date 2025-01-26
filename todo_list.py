todo_list = []

def add_task(title):
    todo_list.append({"title": title, "completed": False})

def view_tasks():
    for idx, task in enumerate(todo_list):
        status = "Done" if task['completed'] else "Not Done"
        print(f"{idx + 1}. {task['title']} - {status}")

def complete_task(index):
    if 0 <= index < len(todo_list):
        todo_list[index]['completed'] = True

print("Welcome to the To-Do List App!")
while True:
    print("\n1. Add Task\n2. View Tasks\n3. Complete Task\n4. Exit")
    choice = int(input("Choose an option: "))

    if choice == 1:
        title = input("Enter task title: ")
        add_task(title)
    elif choice == 2:
        view_tasks()
    elif choice == 3:
        index = int(input("Enter task number to complete: ")) - 1
        complete_task(index)
    elif choice == 4:
        print("Goodbye!")
        break
    else:
        print("Invalid choice!")
