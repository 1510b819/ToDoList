class ToDoList:
    def __init__(self):
        self.tasks = []
        self.loadTasks()  # Load tasks from the file on initialization

    def loadTasks(self):
        try:
            with open("ToDoList.txt", "r") as f:
                self.tasks = f.readlines()
                self.tasks = [task.strip() for task in self.tasks]  # Remove newlines
        except FileNotFoundError:
            self.tasks = []  # No file yet, start with empty tasks

    def saveTasks(self):
        with open("ToDoList.txt", "w") as f:
            for task in self.tasks:
                f.write(f"{task}\n")  # Write each task on a new line

    def createTask(self, title, description):
        newTask = f"title: {title}, description: {description}"
        self.tasks.append(newTask)
        self.saveTasks()  # Save after adding a task

    def deleteTask(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
            self.saveTasks()  # Save after deleting a task
        else:
            raise Exception("Wrong index")

    def updateTask(self, title, description, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index] = f"title: {title}, description: {description}"
            self.saveTasks()  # Save after updating a task
        else:
            raise Exception("Wrong index")

    def viewTasks(self):
        if not self.tasks:
            print("No tasks available.")
        for i in range(len(self.tasks)):
            print(f"{i}: {self.tasks[i]}")

if __name__ == "__main__":
    todo = ToDoList()  # Create an instance of ToDoList

    # Example usage:
    todo.createTask("Buy groceries", "Milk, Eggs, Bread")
    todo.createTask("Clean room", "Dust and vacuum")
    todo.viewTasks()

    todo.updateTask("Buy groceries", "Milk, Eggs, Bread, Butter", 0)
    todo.viewTasks()

    todo.deleteTask(1)
    todo.viewTasks()
