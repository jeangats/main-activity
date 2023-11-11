class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.status = "[Pending]"

    def __str__(self):
        return f"{self.status}\tTitle: {self.title}\n\t\t\tDescription: {self.description}"

class TaskManager:
    def __init__(self):
        self.stack = []
        self.top = -1

    def is_empty(self):
        return self.top == -1

    def push_task(self, title, description):
        task = Task(title, description)
        if task not in self.stack:
            self.top += 1
            self.stack.append(task)
            return "This task has been added to the list."
        else:
            return "This task is already in the list."

    def mark_status(self, title):
        for task in self.stack:
            if task.title == title:
                task.status = "[Completed]"
                return "The status of this task is now marked as completed."
        return "This task is not in the list."

    def display_taskList(self):
        if self.is_empty():
            print("The list is still empty. Please add a task first.")
        else:
            print("\nList of tasks:")
            for task in self.stack:
                print(task)
        return ""

    def display(self):
        while True:
            try:
                print("\n\t\t\t| Task Manager |\n1. Add Tasks with a Title and Description\n2. Mark the Status of Tasks as Completed\n3. Display the List of Tasks along with Status\n4. Exit the task manager")
                menu_option = int(input("Choose from options 1 to 4 from the menu: "))
                print("")
            except ValueError:
                print("Invalid input. Please enter only numbers from 1 to 4.")
                continue

            if menu_option == 1:
                title = input("Enter the title of task: ").lower()
                description = input("Enter the description task: ").lower()
                print(self.push_task(title, description))

            elif menu_option == 2:
                mark = input("Enter task title to mark as completed: ").lower()
                print(self.mark_status(mark))

            elif menu_option == 3:
                print(self.display_taskList())

            elif menu_option == 4:
                print("Exiting Task Manager...")
                break

            else:
                print("\nPlease Try Again... The options in the menu are only from 1 to 4.")


TaskManager().display()