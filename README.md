# Python CLI To-Do List Manager

A simple, lightweight command-line To-Do List application built in Python. It allows users to easily create, view, complete, and persistently store their tasks using a local JSON file.

## Features

- **Interactive Menu:** Clean command-line interface for smooth navigation.
- **Persistent Storage:** Automatically saves and loads tasks using a local `todo_list.json` file so you never lose your progress.
- **Task Tracking:** View tasks categorized by their status (`[Pending]` or `[Completed]`).
- **Error Handling:** Robust input validation to handle empty descriptions and invalid menu or task choices.

## Prerequisites

Make sure you have **Python 3.x** installed on your system. No external packages or libraries are required since it uses Python's built-in `json` module.

## Getting Started

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
   cd your-repo-name
Run the program:

Bash
python main.py
How to Use
When you run the program, you will be presented with a menu options:

View tasks: Displays all current tasks along with their completion status.

Create tasks: Prompts you to enter a description for a new task and adds it to your list.

Complete Task: Shows your task list and prompts you to enter the number of the task you have finished.

Exit: Saves your current data and closes the application.

Code Structure
load_task(): Loads existing tasks from todo_list.json or initializes a new task structure if the file doesn't exist.

save_tasks(tasks): Saves the current state of tasks to the JSON file.

create_task(tasks): Adds a new task with a pending status.

view_tasks(tasks): Formats and displays all tasks in the console.

mark_task_completed(tasks): Updates a specific task's status to completed.

main(): Runs the core application loop.
