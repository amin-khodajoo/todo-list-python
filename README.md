# To-Do List Application

A simple command-line To-Do List application built with Python. Tasks are persisted to a local `myfile.txt` file.

## Features

- **Add Task**: Add a new task to your to-do list
- **Delete Task**: Remove a task from your to-do list
- **View All Tasks**: Print the entire list of tasks
- **Persistent Storage**: Tasks are saved to `myfile.txt` between sessions

## Project Structure

```
todo/
├── main.py           # Entry point with the CLI loop and menu
├── utils/
│   └── todo.py       # ToDoList class with business logic
├── myfile.txt        # Persistent task storage
└── README.md
```

## Requirements

- Python 3.10+ (for `match` / `case` syntax)
- No external dependencies required

## How to Run

```bash
python main.py
```

## Usage

When the application starts, you will see a menu:

```
1) add task
2) delete task
3) print all tasks
4) exit
```

| Option | Action |
|--------|--------|
| 1 | Add a new task (you will be prompted to enter the task description) |
| 2 | Delete an existing task (you will be prompted to enter the task description) |
| 3 | View all current tasks |
| 4 | Exit the application |

## How It Works

- **main.py**: Handles the CLI loop, clears the console between operations, and delegates actions to the `ToDoList` class based on user input.
- **utils/todo.py**: Contains the `ToDoList` class with four methods:
  - `add(task)` — Appends a task to `myfile.txt`
  - `get_all()` — Reads and prints all tasks from `myfile.txt`
  - `delete(item)` — Removes a matching task from `myfile.txt`
  - `show()` (static) — Displays the CLI menu
