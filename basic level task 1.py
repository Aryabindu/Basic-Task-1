def display_menu():
    print("\nTo-Do List Menu")
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Mark Task as Completed")
    print("4. Remove Task")
    print("5. Quit")

def view_list(todo_list):
    if not todo_list:
        print("\nYour to-do list is empty.")
    else:
        print("\nYour To-Do List:")
        for i, (task, completed) in enumerate(todo_list, start=1):
            status = "Completed" if completed else "Incomplete"
            print(f"{i}. {task} - {status}")

def add_task(todo_list):
    task = input("\nEnter the task to add: ")
    todo_list.append((task, False))
    print(f"'{task}' has been added to your to-do list.")

def mark_task_completed(todo_list):
    if not todo_list:
        print("\nYour to-do list is empty.")
        return

    view_list(todo_list)
    try:
        task_number = int(input("\nEnter the number of the task to mark as completed: "))
        if 1 <= task_number <= len(todo_list):
            task, _ = todo_list[task_number - 1]
            todo_list[task_number - 1] = (task, True)
            print(f"'{task}' has been marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def remove_task(todo_list):
    if not todo_list:
        print("\nYour to-do list is empty.")
        return

    view_list(todo_list)
    try:
        task_number = int(input("\nEnter the number of the task to remove: "))
        if 1 <= task_number <= len(todo_list):
            removed_task, _ = todo_list.pop(task_number - 1)
            print(f"'{removed_task}' has been removed from your to-do list.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def main():
    todo_list = []
    while True:
        display_menu()
        choice = input("\nEnter your choice: ")
        if choice == '1':
            view_list(todo_list)
        elif choice == '2':
            add_task(todo_list)
        elif choice == '3':
            mark_task_completed(todo_list)
        elif choice == '4':
            remove_task(todo_list)
        elif choice == '5':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()

