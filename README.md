# Task Tracker

A simple, menu-driven task management application built with Python. Task Tracker helps users organize everyday activities from the command line by creating tasks, editing descriptions, deleting tasks, tracking progress, and filtering tasks by status.

<p align="center">
<img src="./screenshots/pic 1.png" width="900">
</p>

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Built With](#built-with)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Task Statuses](#task-statuses)
- [Data Storage](#data-storage)
- [Known Limitations](#known-limitations)
- [Possible Future Improvements](#possible-future-improvements)
- [Contributing](#contributing)
- [License](#license)

## Overview

Task Tracker is a beginner-friendly Python command-line application for managing a personal task list. It presents an interactive menu so users can perform task-management operations without needing a graphical interface or a database server.

Tasks are saved to a local `tasks.json` file, allowing the application to load saved tasks when it starts again.

## Features

- **Add tasks** with a description.
- **List all tasks** with their ID, description, and status.
- **Update task descriptions**.
- **Delete tasks** by ID.
- **Change task status** to `In Progress` or `Done`.
- **Filter tasks** by status:
  - `Not Done`
  - `In Progress`
  - `Done`
- **Persist task data** in a local JSON file.
- **Validate basic user input**, including empty task descriptions and non-numeric IDs.

## Built With

- **Python 3**
- **JSON** for local data persistence
- Python standard-library modules:
  - `json`
  - `os`

No third-party Python packages are required for the functionality shown in the current implementation.

## Project Structure

```text
task-tracker/
├── task_tracker.py   # Main application and task-management functions
├── tasks.json        # Created automatically when tasks are saved
└── README.md         # Project documentation
```

> `tasks.json` may not exist until you add or modify a task. Keep it in the same working directory from which you run the application.

## Requirements

- Python 3 installed on your computer.
- A terminal or command prompt.
- Git (optional, for version control).

Check that Python is installed:

```bash
python --version
```

Depending on your system, you may need to use:

```bash
python3 --version
```

## Getting Started

### 1. Clone the repository

Clone the project with:

```bash
git clone <https://github.com/Vickysure/Task_Tracker>
```

Move into the project directory:

```bash
cd <task_tracker.py>
```


### 2. Run the application

From the directory containing `task_tracker.py`, run:

```bash
python task_tracker.py
```

If your system uses `python3`, run:

```bash
python3 task_tracker.py
```

The application should display the Task Tracker menu in your terminal.

## Usage

When the program starts, it displays a menu similar to this:

```text
===== TASK TRACKER =====
1. Add a task.
2. Update a task.
3. Delete a task.
4. Change task status.
5. List all tasks.
6. List Completed tasks.
7. List tasks not done.
8. List tasks in progress.
9. Exit.
```

<p align="center">
<img src="./screenshots/pic 2.png" width="900">
</p>

Enter the number for the operation you want to perform, then follow the prompts.

| Menu option | Action |
|---|---|
| `1` | Add a new task |
| `2` | Update a task description |
| `3` | Delete a task |
| `4` | Change a task's status |
| `5` | Display all tasks |
| `6` | Display tasks marked `Done` |
| `7` | Display tasks marked `Not Done` |
| `8` | Display tasks marked `In Progress` |
| `9` | Exit the application |

### Example workflow

1. Select **1** and enter a task description, such as `Attend to School Activities`.
2. Select **5** to view the task and its ID.
3. Select **4**, enter the task ID, and choose a new status:
   - `1` for `In Progress`
   - `2` for `Done`
4. Select **6**, **7**, or **8** to filter tasks by status.
5. Select **9** to exit.

## Task Statuses

<p align="center">
<img src="./screenshots/pic 4.png" width="900">
</p>

Task Tracker uses these status values:

| Status | Meaning |
|---|---|
| `Not Done` | The task has not yet been completed. This is the default status for new tasks. |
| `In Progress` | Work on the task has started but is not yet complete. |
| `Done` | The task has been completed. |

The current menu allows a task to be changed to `In Progress` or `Done`. New tasks are created with the `Not Done` status.

## Data Storage

Task records are stored in `tasks.json` as a JSON array. A task has the following structure:

```json
[
    {
        "id": 1,
        "description": "Attend to School Activities",
        "status": "Not Done"
    }
]
```

<p align="center">
<img src="./screenshots/pic 3.png" width="900">
</p>

Each task contains:

- `id`: a numeric identifier used to select the task.
- `description`: the task's text.
- `status`: the task's current progress state.

The application loads this file at startup and saves changes when tasks are added, updated, deleted, or have their status changed. If the file does not exist, the application starts with an empty task list.

**Data note:** `tasks.json` is a local file. Back it up if the task list is important, and avoid editing it manually unless you understand JSON formatting.

## Known Limitations

The following are limitations to be aware of in the current implementation:

- Tasks are stored locally, so the data is not automatically synchronized across devices.
- There is no graphical user interface; interaction happens in the terminal.
- There are no due dates, priorities, categories, reminders, or user accounts.
- The task filter prints matching task records in their Python dictionary representation rather than using the formatted layout of the full task list.
- The current task-update function contains an ID comparison issue: it compares the task ID with the literal string `"task_id"` instead of the numeric `task_id` entered by the user. As a result, updating a task description will not work as intended until that comparison is corrected.
- The program handles some file-loading errors by returning an empty list. If `tasks.json` is malformed or unreadable, this can make existing tasks appear absent during that run; investigate the file before continuing to make changes.

## Possible Future Improvements

Ideas for future versions include:

- Fix and test task updates.
- Improve the output format for filtered task lists and display a message when no tasks match a status.
- Add due dates and priority levels.
- Add search and sorting.
- Add confirmation before deleting a task.
- Add automated tests with Python's `unittest` or `pytest`.
- Improve error handling for corrupted or inaccessible JSON files.
- Add a graphical interface or web API.
- Add export, backup, and restore options.

## Contributing

Contributions and suggestions are welcome.

1. Fork the repository.
2. Create a branch for your change.
3. Make your changes and test them.
4. Commit with a clear message.
5. Open a pull request describing the improvement.

For a personal learning project, you can also track bugs and ideas using GitHub Issues.

## License

No license is currently specified. If you plan to publish or share this project, choose and add an appropriate open-source license before others reuse or redistribute it.


## Author

***Victor Ukachi Chiemela***
- Email : [ukadovicky07@gmail.com]
- Whatsapp : [+2348104951975]
