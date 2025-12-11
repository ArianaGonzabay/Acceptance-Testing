import datetime

class Task:
    def __init__(self, description, priority="Normal"):
        self.description = description
        self.status = "Pending"
        self.priority = priority
        self.created_at = datetime.datetime.now()

    def __str__(self):
        return f"{self.description} [{self.status}]"

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        new_task = Task(description)
        self.tasks.append(new_task)
        return new_task

    def get_all_tasks(self):
        return self.tasks

    def clear(self):
        self.tasks = []

def main():
    todo_list = TodoList()
    
    while True:
        print("\n--- To-Do List Manager ---")
        print("1. Add Task")
        print("2. Exit")
        
        choice = input("Select an option: ")
        
        if choice == "1":
            description = input("Enter task description: ")
            task = todo_list.add_task(description)
            print(f"Task added: {task}")
        elif choice == "2":
            print("Exiting...")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
