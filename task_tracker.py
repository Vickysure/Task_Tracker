import json
import os

FILE_NAME = "tasks.json"

def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []

    try:
        with open (FILE_NAME,"r") as file:
            return json.load(file)


    except (json.JSONDecodeError, OSError):
        return []

def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent =4)

# function the user to add task

def add_task(tasks):
    description = input ("Enter your task: ").strip()

    if not description:
        print("Task description cannot be empty.")
        return
    
    new_id = max(
        (task["id"] for task in tasks),
        default = 0
    ) + 1

    task ={
        "id" :new_id,
        "description" : description,
        "status": "Not Done"
    }

    tasks.append(task)
    save_tasks(tasks)

    print ("Task added Successfully.")

# function to display all uploaded task

def list_tasks(tasks):
    if not tasks:
        print ("No tasks found.")
        return

    for task in tasks:
        print(
            f"ID: {task['id']} | "
            f"Task: {task['description']} | "
            f"Status: {task['status']}"
        )

# function to separate/ filter task by its status

def filter_tasks(tasks, status):
    for task in tasks:
        if task["status"] == status:
            print (task)

    """we could call the function, using this format;
# filter_tasks (tasks, "Done")
# filter_tasks (tasks, "Not Done")
# filter_tasks (tasks, "In Progress")
"""


# function to update a task list

def update_tasks(tasks):
    try:
        task_id = int (input("Enter the ID of the task to Update: "))

    except ValueError:
        print("Please enter a valid Number")
        return

    for task in tasks:
        if task["id"] == "task_id":
            new_description = input(
                "Enter the new task description:"
            ).strip()

            if not new_description:
                print ("task description cannot be Empty.")
                return
            task["description"] = new_description
            save_tasks(tasks)

            print("Task Updated Successfully")
            return
    print ("Task ID not Found.")

# function to remove or delete unwanted task

def delete_tasks(tasks):
    try:
        task_id = int(input("Enter the task ID to be deleted: "))

    except ValueError:
        print("Please enter a valid task ID.")
        return

    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            save_tasks(tasks)

            print("Task deleted Successfully.")
            return

    print("Task ID not Found.")


# function to change a task status

def change_task_status(tasks):
    try:
        task_id = int(input("Enter the task ID:"))

    except ValueError:
        print ("Please Enter a Valid number.")
        return

    task = None

    for item in tasks:
        if item["id"] == task_id:
            task = item
            break

    if task is None:
        print ("Task is not found.")
        return

    print("1. In Progress")
    print("2. Done")

    choice = input ("Choose the New Status.").strip()

    if choice == "1":
        task["status"] = "In Progress"

    elif choice == "2":
        task["status"] = "Done"

    else:
        print ("Invalid status choice.")
        return

    save_tasks(tasks)
    print("Task Status Updated Successfully.")


# function to connect all sections into a menu

def menu():
    tasks = load_tasks()

    while True:
        print ("\n===== TASK TRACKER =====")
        print ("1. Add a task.")
        print ("2. Update a task.")
        print ("3. Delete a task.")
        print ("4. Change task status.")
        print ("5. List all tasks.")
        print ("6. List Completed tasks.")
        print ("7. List tasks not done.")
        print ("8. List tasks in progress.")
        print ("9. Exit.")

        choice = input ("Choose an option (1-9)\n").strip()

        if choice == "1":
            add_task(tasks)

        elif choice == "2":
            update_tasks(tasks)

        elif choice == "3":
            delete_tasks(tasks)

        elif choice == "4":
            change_task_status(tasks)

        elif choice == "5":
            list_tasks(tasks)

        elif choice == "6":
            filter_tasks(tasks, "Done")

        elif choice == "7":
            filter_tasks(tasks, "Not Done")

        elif choice == "8":
            filter_tasks(tasks, "In Progress")

        elif choice == "9":
            print ("Thank You for using TASK TRACKER!.")
            break

        else:
            print ("Invalid Choice, Please choose from 1 to 9.")


if __name__ == "__main__":
    menu()