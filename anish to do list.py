tasks = []

def add_task(new_task):
  
    
    tasks.append(new_task)
    print(f"Added task: {new_task}")

def remove_task(task_to_remove):
   
    if task_to_remove in tasks:
        tasks.remove(task_to_remove)
        print(f"Removed task: {task_to_remove}")
    else:
        print(f"{task_to_remove} not found")

def view_tasks():
   
    
    print("To-Do List:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

#
while True:
    print("\nWhat do you want to do?")
    print("1. Add a task")
    print("2. Remove a task")
    print("3. View all tasks")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        new_task = input("Enter a new task: ")
        add_task(new_task)
    elif choice == "2":
        task_to_remove = input("Enter task to remove: ")
        remove_task(task_to_remove)
    elif choice == "3":
        view_tasks()
    elif choice == "4":
        print("Exiting")
        break
    else:
        print("Invalid choice!")
