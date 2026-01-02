"""
Module for managing todo tasks.
This module contains the Task class and TodoManager class.
"""
from typing import List, Optional


class Task:
    """Represents a single task in the todo list."""

    def __init__(self, task_id: int, title: str, description: str = ""):
        """
        Initialize a Task instance.

        Args:
            task_id: Unique identifier for the task
            title: Title of the task (required)
            description: Description of the task (optional)
        """
        if not isinstance(task_id, int) or task_id <= 0:
            raise ValueError("Task ID must be a positive integer")
        if not title or not title.strip():
            raise ValueError("Title cannot be empty")
        if len(title) > 100:
            raise ValueError("Title must be 100 characters or less")
        if len(description) > 500:
            raise ValueError("Description must be 500 characters or less")

        self.id = task_id
        self.title = title.strip()
        self.description = description.strip()
        self.completed = False


class TodoManager:
    """Manages a collection of tasks."""

    def __init__(self):
        """Initialize a TodoManager instance."""
        self.tasks: List[Task] = []
        self.next_id = 1

    def add_task(self, title: str, description: str = "") -> Task:
        """
        Add a new task to the todo list.

        Args:
            title: Title of the task
            description: Description of the task (optional)

        Returns:
            The newly created Task object
        """
        # Validate inputs
        if not title.strip():
            raise ValueError("Title cannot be empty")
        if len(title) > 100:
            raise ValueError("Title must be 100 characters or less")
        if len(description) > 500:
            raise ValueError("Description must be 500 characters or less")

        # Create new task
        task = Task(self.next_id, title, description)
        self.tasks.append(task)
        self.next_id += 1
        return task

    def view_tasks(self) -> List[Task]:
        """
        Get all tasks in the todo list.

        Returns:
            A list of all Task objects
        """
        return self.tasks.copy()  # Return a copy to prevent external modification

    def update_task(self, task_id: int, new_title: Optional[str] = None, new_description: Optional[str] = None) -> Task:
        """
        Update an existing task's title and/or description.

        Args:
            task_id: ID of the task to update
            new_title: New title for the task (optional)
            new_description: New description for the task (optional)

        Returns:
            The updated Task object
        """
        # Find the task
        task = self._find_task_by_id(task_id)
        if not task:
            raise ValueError(f"Task with ID {task_id} not found")

        # Update title if provided
        if new_title is not None:
            if not new_title.strip():
                raise ValueError("Title cannot be empty")
            if len(new_title) > 100:
                raise ValueError("Title must be 100 characters or less")
            task.title = new_title

        # Update description if provided
        if new_description is not None:
            if len(new_description) > 500:
                raise ValueError("Description must be 500 characters or less")
            task.description = new_description

        return task

    def delete_task(self, task_id: int) -> bool:
        """
        Delete a task from the todo list.

        Args:
            task_id: ID of the task to delete

        Returns:
            True if the task was deleted, False if not found
        """
        task = self._find_task_by_id(task_id)
        if not task:
            raise ValueError(f"Task with ID {task_id} not found")

        self.tasks.remove(task)
        return True

    def mark_task_complete(self, task_id: int) -> Task:
        """
        Toggle the completion status of a task.

        Args:
            task_id: ID of the task to mark

        Returns:
            The updated Task object
        """
        task = self._find_task_by_id(task_id)
        if not task:
            raise ValueError(f"Task with ID {task_id} not found")

        task.completed = not task.completed
        return task

    def _find_task_by_id(self, task_id: int) -> Optional[Task]:
        """
        Helper method to find a task by its ID.

        Args:
            task_id: ID of the task to find

        Returns:
            The Task object if found, None otherwise
        """
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None