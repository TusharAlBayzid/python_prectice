import json
import datetime
import random
import os

class Task:
    def __init__(self, title, description, id=None, created_at=None):
        self.id = id if id else random.randint(1000, 9999) 
        self.title = title
        self.description = description
        
        if created_at is None:
            self.created_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        else:
            self.created_at = created_at

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "created_at": self.created_at
        }
    
    def __str__(self):
        return f"[ID: {self.id}] {self.title}\n  Created: {self.created_at}\n  Description: {self.description}"


class TaskManager:
    def __init__(self, file_name="tasks.json"):
        self.file_name = file_name
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        if not os.path.exists(self.file_name):
            print("INFO: Task file not found. Starting with empty list.")
            return

        try:
            with open(self.file_name, 'r', encoding='utf-8') as f:
                data = json.load(f)
                for d in data:
                    self.tasks.append(Task(d['title'], d['description'], d['id'], d['created_at']))
            print(f"INFO: Loaded {len(self.tasks)} tasks.")
        
        except json.JSONDecodeError:
            print(f"ERROR: Task file is corrupted. Starting new list.")
        except Exception:
            print(f"ERROR: An unknown issue occurred during loading.")

    def save_tasks(self):
        data = [task.to_dict() for task in self.tasks]
        
        try:
            with open(self.file_name, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=4)
            print(f"INFO: All tasks saved to {self.file_name}.")
        except Exception:
            print(f"ERROR: Failed to save tasks.")
            
    def _find_index(self, task_id):
        try:
            task_id = int(task_id)
        except ValueError:
            return -1
            
        for i, task in enumerate(self.tasks):
            if task.id == task_id:
                return i
        return -1

    def add_task(self, title, description):
        new_task = Task(title, description)
        self.tasks.append(new_task)
        print(f"SUCCESS: Task added with ID: {new_task.id}")

    def view_tasks(self):
        if not self.tasks:
            print("INFO: No tasks found.")
            return

        print("\n--- Current Task List ---")
        for task in self.tasks:
            print(task)
            print("-" * 35)

    def update_task(self, task_id, new_title, new_description):
        index = self._find_index(task_id)

        if index == -1:
            print(f"ERROR: Task ID {task_id} not found.")
            return

        task = self.tasks[index]
        task.title = new_title
        task.description = new_description
        print(f"SUCCESS: Task ID {task_id} updated.")

    def delete_task(self, task_id):
        index = self._find_index(task_id)

        if index == -1:
            print(f"ERROR: Task ID {task_id} not found.")
            return

        deleted_task = self.tasks.pop(index)
        print(f"SUCCESS: Task '{deleted_task.title}' (ID: {task_id}) deleted.")

    def run(self):
        while True:
            print("\n===== Student Task Tracker =====")
            print("1. Add New Task")
            print("2. View All Tasks")
            print("3. Update Task")
            print("4. Delete Task")
            print("5. Exit")
            print("================================")

            choice = input("Enter your choice (1-5): ")

            if choice == '1':
                title = input("Enter Task Title: ")
                description = input("Enter Task Description: ")
                self.add_task(title, description)

            elif choice == '2':
                self.view_tasks()

            elif choice == '3':
                self.view_tasks()
                task_id = input("Enter Task ID to update: ")
                new_title = input("Enter new Title: ")
                new_description = input("Enter new Description: ")
                self.update_task(task_id, new_title, new_description)

            elif choice == '4':
                self.view_tasks()
                task_id = input("Enter Task ID to delete: ")
                self.delete_task(task_id)

            elif choice == '5':
                self.save_tasks()
                print("Application shutting down. Goodbye!")
                break

            else:
                print("ERROR: Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    manager = TaskManager()
    manager.run()
    
    