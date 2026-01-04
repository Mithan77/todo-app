# Todo App

A simple command-line todo application built with Python. This application allows you to manage your tasks efficiently with features to add, view, update, delete, and mark tasks as complete or incomplete.

## Features

- Add new tasks with title and description
- View all tasks with their completion status
- Update existing tasks
- Delete tasks
- Mark tasks as complete/incomplete
- Input validation for task titles and descriptions
- Persistent task management within a session

## Prerequisites

- Python 3.7 or higher

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/Mithan77/todo-app.git
   ```

2. Navigate to the project directory:
   ```bash
   cd todo-app
   ```

3. Navigate to the src directory:
   ```bash
   cd src
   ```

4. Run the application:
   ```bash
   python main.py
   ```

## Usage

Once you run the application, you'll see a menu with the following options:

1. **Add task** - Create a new task by providing a title and description
2. **View tasks** - See all your tasks with their completion status
3. **Update task** - Modify the title or description of an existing task
4. **Delete task** - Remove a task from your list
5. **Mark task as complete/incomplete** - Toggle the completion status of a task
6. **Exit** - Close the application

### Task Validation

- Task titles must be between 1 and 100 characters
- Task descriptions can be up to 500 characters
- Task IDs must be positive integers

## Project Structure

```
todo-app/
├── src/
│   ├── main.py          # Main application entry point
│   └── todo_manager.py  # Task management logic
└── README.md
```

## Code Overview

### TodoManager Class

The `TodoManager` class handles all task operations:

- `add_task(title, description)` - Adds a new task
- `view_tasks()` - Returns all tasks
- `update_task(task_id, new_title, new_description)` - Updates a task
- `delete_task(task_id)` - Deletes a task
- `mark_task_complete(task_id)` - Toggles task completion status

### Task Class

The `Task` class represents a single task with:

- `id` - Unique identifier
- `title` - Task title
- `description` - Task description
- `completed` - Boolean indicating completion status

## Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add some amazing feature'`)
5. Push to the branch (`git push origin feature/amazing-feature`)
6. Open a Pull Request

## License

This project is open source and available under the [MIT License](LICENSE).

## Contact

If you have any questions or suggestions, feel free to contact me or open an issue in the repository.