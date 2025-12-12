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

    def delete_task(self, description):
        for t in self.tasks:
            if t.description == description:
                self.tasks.remove(t)
                return True
        return False

    def mark_as_completed(self, position):
        if isinstance(position, str):
            position = int(position)
        position -= 1
        if position in range(len(self.tasks)):
            self.tasks[position].status = "Completed"
            return True
        return False


def main():
    todo_list = TodoList()

    while True:
        print("\n--- To-Do List Manager ---")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Mark A Task as Completed")
        print("4. Delete a Task")
        print("5. Clear All Tasks")
        print("6. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            description = input("Enter task description: ")
            task = todo_list.add_task(description)
            print(f"Task added: {task}")

        elif choice == "2":
            for i, task in enumerate(todo_list.tasks):
                print(f"{i+1}. {task.description} [{task.status}]")

        elif choice == "3":
            for i in range(len(todo_list.tasks)):
                print(f"{i+1}. {todo_list.tasks[i].description}")
            position = input("Enter the number of the task to complete: ")
            if todo_list.mark_as_completed(position):
                print("Task marked successfully.")
            else:
                print("Invalid number.")

        elif choice == "4":
            desc = input("Enter the task description to delete: ")
            if todo_list.delete_task(desc):
                print("Task deleted.")
            else:
                print("Task not found.")

        elif choice == "5":
            todo_list.clear()
            print("All tasks cleared.")

        elif choice == "6":
            print("Exiting...")
            break

        else:
            print("Invalid option, try again.")

if __name__ == "__main__":
    main()
