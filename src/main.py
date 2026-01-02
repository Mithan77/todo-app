"""
Main module for the Todo App.
This module contains the main application loop and user interface.
"""
from todo_manager import TodoManager


def main():
    """
    Main application loop for the Todo App.
    """
    print("Welcome to the Todo App!")
    todo_manager = TodoManager()
    
    while True:
        print("\nPlease select an option:")
        print("1. Add task")
        print("2. View tasks")
        print("3. Update task")
        print("4. Delete task")
        print("5. Mark task as complete/incomplete")
        print("6. Exit")
        
        choice = input("Choose an option: ").strip()
        
        if choice == "1":
            add_task_ui(todo_manager)
        elif choice == "2":
            view_tasks_ui(todo_manager)
        elif choice == "3":
            update_task_ui(todo_manager)
        elif choice == "4":
            delete_task_ui(todo_manager)
        elif choice == "5":
            mark_task_ui(todo_manager)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")


def add_task_ui(todo_manager):
    """UI for adding a new task."""
    title = input("Enter task title: ").strip()
    description = input("Enter task description: ").strip()

    try:
        task = todo_manager.add_task(title, description)
        print(f"Task added successfully with ID: {task.id}")
    except ValueError as e:
        print(f"Error: {e}")


def view_tasks_ui(todo_manager):
    """UI for viewing all tasks."""
    tasks = todo_manager.view_tasks()
    if not tasks:
        print("No tasks yet. Add some tasks.")
        return

    print("\nYour tasks:")
    for task in tasks:
        status = "[x]" if task.completed else "[ ]"
        print(f"{status} ID: {task.id} | Title: {task.title} | Description: {task.description}")


def update_task_ui(todo_manager):
    """UI for updating a task."""
    try:
        task_id_input = input("Enter task ID to update: ").strip()
        if not task_id_input:
            print("Task ID cannot be empty.")
            return
        task_id = int(task_id_input)
    except ValueError:
        print("Invalid ID. Please enter a number.")
        return

    # Get current task details
    tasks = todo_manager.view_tasks()
    task = next((t for t in tasks if t.id == task_id), None)
    if not task:
        print("Task not found.")
        return

    print(f"Current title: {task.title}")
    new_title = input("New title (leave empty to keep current): ").strip()
    if new_title == "":
        new_title = None

    print(f"Current description: {task.description}")
    new_description = input("New description (leave empty to keep current): ").strip()
    if new_description == "":
        new_description = None

    try:
        updated_task = todo_manager.update_task(task_id, new_title, new_description)
        print("Task updated successfully.")
    except ValueError as e:
        print(f"Error: {e}")


def delete_task_ui(todo_manager):
    """UI for deleting a task."""
    try:
        task_id_input = input("Enter task ID to delete: ").strip()
        if not task_id_input:
            print("Task ID cannot be empty.")
            return
        task_id = int(task_id_input)
    except ValueError:
        print("Invalid ID. Please enter a number.")
        return

    try:
        todo_manager.delete_task(task_id)
        print("Task deleted successfully.")
    except ValueError as e:
        print(f"Error: {e}")


def mark_task_ui(todo_manager):
    """UI for marking a task as complete/incomplete."""
    try:
        task_id_input = input("Enter task ID to mark: ").strip()
        if not task_id_input:
            print("Task ID cannot be empty.")
            return
        task_id = int(task_id_input)
    except ValueError:
        print("Invalid ID. Please enter a number.")
        return

    try:
        task = todo_manager.mark_task_complete(task_id)
        status = "complete" if task.completed else "incomplete"
        print(f"Task marked as {status}.")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()