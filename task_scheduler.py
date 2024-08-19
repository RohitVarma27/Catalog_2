import json
import os

class TaskScheduler:
    def __init__(self):
        self.file_path = "data/tasks.json"
        self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                self.tasks = json.load(file)
        else:
            self.tasks = []

    def save_tasks(self):
        with open(self.file_path, 'w') as file:
            json.dump(self.tasks, file)

    def add_task(self):
        task_description = input("Enter task description: ")
        due_date = input("Enter due date: ")

        task = {
            "description": task_description,
            "due_date": due_date
        }

        self.tasks.append(task)
        self.save_tasks()
        print("Task added successfully!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks scheduled.")
        else:
            for task in self.tasks:
                print(f"Task: {task['description']}, Due Date: {task['due_date']}")

    def schedule_tasks(self):
        while True:
            print("\nTask Scheduler")
            print("1. Add Task")
            print("2. View Tasks")
            print("3. Back")

            choice = input("Select an option: ")

            if choice == "1":
                self.add_task()
            elif choice == "2":
                self.view_tasks()
            elif choice == "3":
                break
            else:
                print("Invalid choice, please try again.")
