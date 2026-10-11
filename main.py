# Load existing data 
# This is a to-do list program
# first function. create a new item
# second function. List items
# third function. Mark item as complete 
# fourth function. save items

import json 

file_name = "todo_list.json"

def load_task():
    try:
        with open(file_name, "r") as file:
            return json.load(file)
    except:
        return {"tasks": []}

def save_tasks(tasks):
    try:
        with open(file_name, "w") as file:
            return json.dump(tasks, file)
    except:
        print("Failed to save.")
        

def create_task(tasks):
    description = input("Enter the task description: ").strip()
    if description:
        tasks["tasks"].append({"description": description, "complete": False})
        save_tasks(tasks)
        print("Task added.")
    else: 
        print("Description cannot be empty.")

def view_tasks(tasks):
    print()
    tasks_list = tasks["tasks"]
    if len(tasks_list) == 0:
        print("No task to display")
    else:
        print("Your TO-DO list: ")
        for idx, task in enumerate(tasks_list):
            status = "[Completed]" if task["complete"] else "[Pending]"
            print(f"{idx + 1}. {task['description']} | {status}")

def mark_task_completed(tasks):
    view_tasks(tasks)
    try:
        task_number = int(input("Enter the task number to mark: ").strip())
        if 1 <= task_number <= len(tasks):
                tasks["tasks"][task_number - 1]["complete"] = True
                save_tasks(tasks)
                print("Task marked as complete")
        else: 
                print("Invalid task number.")
    except:
        print("Enter a valid number.")


def main(): 
    tasks = load_task() 
    

    while True:
        print("\nTo-Do list Manager")
        print("1. View tasks")
        print("2. Create tasks")
        print("3. Complete Task")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            create_task(tasks)
        elif choice == "3":
            mark_task_completed(tasks)
        elif choice == "4":
            print("Goodbye")
            break 
        else: 
            print("Invalid choice.")

main()

