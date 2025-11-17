# Task Manager - Simple CRUD Program

tasks = []

def show_menu():
    print("\n=== TASK MANAGER ===")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

def add_task():
    task = input("Enter new task: ").strip()
    if task:
        tasks.append(task)
        print("Task added successfully!")
    else:
        print("Task cannot be empty.")

def view_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def update_task():
    view_tasks()
    if tasks:
        try:
            index = int(input("\nEnter task number to update: ")) - 1
            if 0 <= index < len(tasks):
                new_task = input("Enter updated task: ").strip()
                if new_task:
                    tasks[index] = new_task
                    print("Task updated successfully!")
                else:
                    print("Task cannot be empty.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def delete_task():
    view_tasks()
    if tasks:
        try:
            index = int(input("\nEnter task number to delete: ")) - 1
            if 0 <= index < len(tasks):
                deleted = tasks.pop(index)
                print(f"Deleted task: '{deleted}'")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-5): ")
        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            update_task()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("Exiting Task Manager. Goodbye!")
            break
        else:
            print("Invalid option, please choose again.")

if __name__ == "__main__":
    main()
