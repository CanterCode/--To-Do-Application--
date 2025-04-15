
tasks = ["Finish Project", "Read Book", "Make Bed", "Go to Gym"]

def display_menu():
    print("\nTodo List Application")
    print("1. Add Task")
    print("2. Delete Task")
    print("3. View Tasks")
    print("4. Exit Application")
    
    
def add_task():
    task = input("What task would you like to add to your list? ")
    tasks.append(task)
    print(f"'{task}' has been added to your list.")
    print(f"Your current tasks are: {tasks}")

def delete_task():
    pass
    
def view_tasks():
    if not tasks:
        print("You have no open tasks.")
    else:
        print("\nHere are your current tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def main():
    
    while True:
    
        display_menu()
        
        choice = input("what would you like to do? ")
        
        if choice == "1":
            add_task()
        
        elif choice == "2":
            delete_task()
        
        elif choice == "3":
            view_tasks()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
    
main()