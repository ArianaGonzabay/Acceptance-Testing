# todo_list.py
from dataclasses import dataclass, asdict
from typing import List, Optional
from datetime import datetime

@dataclass
class Task:
    title: str
    description: str = ""
    due_date: Optional[str] = None  # ISO string or free text
    status: str = "Pending"         # "Pending" or "Completed"

    def to_string(self) -> str:
        due = f" | Due: {self.due_date}" if self.due_date else ""
        return f"{self.title} [{self.status}]{due} - {self.description}".strip()

class ToDoList:
    def __init__(self):
        self.tasks: List[Task] = []

    def add_task(self, title: str, description: str = "", due_date: Optional[str] = None):
        if self._find_task(title) is not None:
            raise ValueError(f"Task with title '{title}' already exists")
        t = Task(title=title, description=description, due_date=due_date, status="Pending")
        self.tasks.append(t)

    def list_tasks(self) -> List[str]:
        # return readable strings for each task
        return [t.to_string() for t in self.tasks]

    def mark_completed(self, title: str) -> bool:
        t = self._find_task(title)
        if t:
            t.status = "Completed"
            return True
        return False

    def clear_tasks(self):
        self.tasks = []

    def delete_task(self, title: str) -> bool:
        t = self._find_task(title)
        if t:
            self.tasks.remove(t)
            return True
        return False

    def _find_task(self, title: str) -> Optional[Task]:
        for task in self.tasks:
            if task.title == title:
                return task
        return None

    # helpers for tests:
    def get_titles(self) -> List[str]:
        return [t.title for t in self.tasks]

    def get_status(self, title: str) -> Optional[str]:
        t = self._find_task(title)
        return t.status if t else None

# Optional quick CLI runner (usable for manual verification)
def main():
    todo = ToDoList()
    print("Simple To-Do List Manager (type 'help' for commands)")
    while True:
        cmd = input("> ").strip()
        if not cmd:
            continue
        parts = cmd.split(maxsplit=1)
        op = parts[0].lower()
        arg = parts[1] if len(parts) > 1 else ""
        try:
            if op in ("exit", "quit"):
                break
            elif op == "help":
                print("Commands: add <title> | addfull <title>|<desc>|<due> | list | complete <title> | delete <title> | clear | exit")
            elif op == "add":
                todo.add_task(arg)
                print("Added.")
            elif op == "addfull":
                # usage: addfull title|desc|due
                a = arg.split("|")
                title = a[0].strip()
                desc = a[1].strip() if len(a) > 1 else ""
                due = a[2].strip() if len(a) > 2 else None
                todo.add_task(title, description=desc, due_date=due)
                print("Added (full).")
            elif op == "list":
                for line in todo.list_tasks():
                    print(" -", line)
            elif op == "complete":
                ok = todo.mark_completed(arg)
                print("Marked." if ok else "Not found.")
            elif op == "delete":
                ok = todo.delete_task(arg)
                print("Deleted." if ok else "Not found.")
            elif op == "clear":
                todo.clear_tasks()
                print("Cleared.")
            else:
                print("Unknown command. type 'help'")
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    main()
